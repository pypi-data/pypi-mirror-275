from __future__ import annotations

from dataclasses import dataclass
from typing import *  # type: ignore

import introspection.types
import introspection.typing

from . import parsers

__all__ = [
    "Unset",
    "UNSET",
    "CommonMetadata",
    "Docstring",
    "FunctionParameter",
    "FunctionDocs",
    "ClassField",
    "ClassDocs",
    "Property",
]


class Unset:
    pass


UNSET = Unset()


@dataclass
class CommonMetadata:
    """
    Some metadata such as whether an object is public or not is shared between
    different types of objects. This class is used to hold that metadata.
    """

    # Whether the object is meant to be used by users of the library, or if it's
    # an internal implementation detail.
    public: bool

    # If `True`, this object is not yet ready for public use. Its API may change
    # between even patch releases.
    experimental: bool

    @staticmethod
    def _parse_bool(
        metadata: dict[str, str],
        key_name: str,
        default_value: bool | None,
    ) -> bool:
        """
        Attempts to parse a boolean value from metadata.

        ## Raises

        `ValueError`: If the key is missing or invalid.
        """

        # Try to get the value
        try:
            raw = metadata[key_name]
        except KeyError:
            # No value provided
            if default_value is None:
                raise ValueError(f"Missing value for `{key_name}` in metadata")

            return default_value

        # Postprocess the value
        if isinstance(raw, str):
            raw = raw.strip()

        # Recognized strings
        if raw == "True":
            return True

        if raw == "False":
            return False

        # Invalid value
        raise ValueError(f'Invalid value for `{key_name}` in metadata: "{raw}"')

    @staticmethod
    def _parse_literal(
        metadata: dict[str, str],
        key_name: str,
        options: Set[str],
        default_value: str | None,
    ) -> str:
        """
        Attempts to parse a literal value from metadata.

        ## Raises

        `ValueError`: If the key is missing or invalid.
        """

        # Try to get the value
        try:
            raw = metadata[key_name]
        except KeyError:
            # No value provided
            if default_value is None:
                raise ValueError(f"Missing value for `{key_name}` in metadata")

            return default_value

        # Postprocess the value
        if isinstance(raw, str):
            raw = raw.strip()

        # Check if the value is valid
        if raw not in options:
            raise ValueError(f'Invalid value for `{key_name}` in metadata: "{raw}"')

        return raw

    @staticmethod
    def from_dictionary(metadata: dict[str, Any]) -> CommonMetadata:
        """
        Parses a `CommonMetadata` object from a dictionary. This is useful for
        parsing metadata from a docstring key section.
        """

        # Parse all values
        public = CommonMetadata._parse_bool(metadata, "public", default_value=True)
        experimental = CommonMetadata._parse_bool(
            metadata, "experimental", default_value=False
        )

        # Construct the result
        return CommonMetadata(
            public=public,
            experimental=experimental,
        )


@dataclass
class FunctionMetadata(CommonMetadata):
    @staticmethod
    def from_dictionary(metadata: dict[str, Any]) -> FunctionMetadata:
        result = CommonMetadata.from_dictionary(metadata)
        result.__class__ = FunctionMetadata
        assert isinstance(result, FunctionMetadata)
        return result


@dataclass
class ClassMetadata(CommonMetadata):
    @staticmethod
    def from_dictionary(metadata: dict[str, Any]) -> ClassMetadata:
        result = CommonMetadata.from_dictionary(metadata)
        result.__class__ = ClassMetadata
        assert isinstance(result, ClassMetadata)
        return result


@dataclass
class Docstring:
    """
    A generic docstring object.

    Docstrings are split into multiple sections: The **summary** is a brief,
    one-line description of the object. This is intended to be displayed right
    next to the object's name in a list of objects for example.

    The **details** section is a more in-depth explanation of the object. This
    may span multiple paragraphs and gives an explanation of the object

    Finally, **key_sections** are sections which consist entirely of `key:
    value` pairs. These can be used for raised exceptions, parameters, and
    similar.
    """

    summary: str | None
    details: str | None

    key_sections: dict[str, dict[str, str]]

    @staticmethod
    def from_string(
        docstring: str,
        *,
        key_sections: Iterable[str],
    ) -> Docstring:
        return parsers.parse_docstring(
            docstring,
            key_sections=key_sections,
        )


@dataclass
class FunctionParameter:
    name: str
    type: introspection.types.TypeAnnotation | Unset
    default: Any | Unset

    kw_only: bool

    collect_positional: bool
    collect_keyword: bool

    description: str | None


@dataclass
class FunctionDocs:
    """
    A docstring specifically for functions and methods.
    """

    object: Callable

    name: str
    parameters: list[FunctionParameter]
    return_type: introspection.types.TypeAnnotation | Unset
    synchronous: bool
    class_method: bool
    static_method: bool

    summary: str | None
    details: str | None

    raises: list[tuple[str, str]]  # type, description

    metadata: FunctionMetadata

    @staticmethod
    def from_function(func: Callable) -> FunctionDocs:
        """
        Parses a `FunctionDocs` object from a function or method. This takes
        both the function's docstring as well as its signature and type hints
        into account.
        """
        return parsers.parse_function(func)


@dataclass
class ClassField:
    name: str
    type: introspection.types.TypeAnnotation | Unset
    default: str | None

    description: str | None


@dataclass
class Property:
    name: str
    getter: FunctionDocs
    setter: FunctionDocs | None

    @staticmethod
    def from_property(prop: property) -> Property:
        assert prop.fget is not None
        getter = FunctionDocs.from_function(prop.fget)

        if prop.fset is None:
            setter = None
        else:
            setter = FunctionDocs.from_function(prop.fset)

        return Property(
            name=getter.name,
            getter=getter,
            setter=setter,
        )


@dataclass
class ClassDocs:
    """
    A docstring specifically for classes.
    """

    object: type

    name: str
    attributes: list[ClassField]
    properties: list[Property]
    functions: list[FunctionDocs]

    summary: str | None
    details: str | None

    metadata: ClassMetadata

    @staticmethod
    def from_class(typ: Type) -> ClassDocs:
        """
        Parses a `ClassDocs` object from a class. This takes both the class's
        docstring as well as its methods and attributes into account.
        """

        return parsers.parse_class(typ)
