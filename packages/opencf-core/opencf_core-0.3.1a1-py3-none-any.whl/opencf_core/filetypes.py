"""
File Type Definitions Module

This module provides a comprehensive framework for handling various file types within a file conversion context.
It defines classes and enumerations for identifying, validating, and working with different file types, based on
file extensions, MIME types, and optionally, file content. It also includes custom exceptions for handling common
errors related to file type processing.

Classes:
- UnsupportedFileTypeError: Custom exception for handling unsupported file types.
- EmptySuffixError: Specialized exception for cases where a file's suffix does not provide enough information
                    to determine its type.
- FileNotFoundError: Raised when a specified file does not exist.
- MismatchedException: Exception for handling cases where there's a mismatch between expected and actual file attributes.
- FileType: Enum class that encapsulates various file types supported by the system, providing methods for
                type determination from file attributes.

Functions:
- test_file_type_parsing(): Demonstrates and validates the parsing functionality for various file types.
- test_file_type_matching(): Tests the matching and validation capabilities of the FileType class.

Dependencies:
- collections.namedtuple: For defining simple classes for storing MIME type information.
- enum.Enum: For creating the FileType enumeration.
- pathlib.Path: For file path manipulations and checks.
- opencf_core.mimes.guess_mime_type_from_file: Utility function to guess MIME type from a file path.

Usage Examples:
```python
from pathlib import Path
from mymodule import FileType, EmptySuffixError, UnsupportedFileTypeError

# Example: Determine file type from suffix
try:
    file_type, _ = FileType.from_suffix('.txt')
    print(f'File type: {file_type.name}')
except (EmptySuffixError, UnsupportedFileTypeError) as e:
    print(f'Error: {e}')

# Example: Determine file type from MIME type
try:
    file_path = Path('/path/to/file.txt')
    file_type, _ = FileType.from_mimetype(file_path)
    print(f'File type: {file_type.name}')
except FileNotFoundError as e:
    print(f'Error: {e}')
except UnsupportedFileTypeError as e:
    print(f'Error: {e}')

# Example: Validate file type by path and content
file_path = Path('/path/to/file.txt')
is_valid = FileType.TEXT.is_valid_path(file_path, read_content=True)
print(f'Is valid: {is_valid}')
```
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Iterable, Tuple, Type, Union

from aenum import extend_enum  # type: ignore

from opencf_core.exceptions import (
    EmptySuffixError,
    MismatchedException,
    UnsupportedFileTypeError,
)

from .mimes import guess_mime_type_from_file

if TYPE_CHECKING:
    # this is only processed by MyPy (i.e. not at runtime)
    from enum import Enum
else:
    # this is real runtime code
    from aenum import Enum


@dataclass(eq=False, frozen=True)
class MimeType:
    """Class representing MIME type information.

    Attributes:
        extensions (Tuple[str, ...]): Tuple of file extensions associated with the MIME type.
        mime_types (Tuple[str, ...]): Tuple of MIME types.
        upper_mime_types (Tuple[str, ...]): Tuple of additional MIME types that can be considered equivalent.
    """

    extensions: Tuple[str, ...] = ()
    mime_types: Tuple[str, ...] = ()
    upper_mime_types: Tuple[str, ...] = ()


class FileType(Enum):
    """Base enumeration for file types, providing methods for type determination and validation.

    Attributes:
        NOTYPE (MimeType): Represents an undefined file type.
        TEXT (MimeType): Represents a text file type.
        UNHANDLED (MimeType): Represents an unhandled file type.
    """

    NOTYPE: MimeType = MimeType()
    TEXT = MimeType(("txt",), ("text/plain",))
    UNHANDLED: MimeType = MimeType()

    def get_value(self) -> MimeType:
        """Returns the `MimeType` associated with the enumeration member.

        Returns:
            MimeType: The MIME type information.
        """
        return self.value  # type:ignore

    @classmethod
    def get_filetypes(cls):
        """Yields all valid file types in the enumeration."""
        for member in cls:
            if not isinstance(member.get_value(), MimeType):
                continue
            yield member

    @classmethod
    def clean_suffix(cls, suffix: str) -> str:
        return suffix.lower().lstrip(".")

    @classmethod
    def from_suffix(
        cls, suffix: str, raise_err: bool = False, return_matches: bool = False
    ) -> Tuple[FileType, Tuple[FileType, ...]]:
        """Determines a filetype from a file's suffix.

        Args:
            suffix (str): The file suffix (extension).
            raise_err (bool, optional): Whether to raise an exception if the type is unhandled. Defaults to False.
            return_matches (bool, optional): Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

        Returns:
            FileType: The determined filetype enumeration member, or a tuple with the first matching filetype and a list of all options.

        Raises:
            EmptySuffixError: If the suffix is empty and raise_err is True.
            UnsupportedFileTypeError: If the file type is unhandled and raise_err is True.
        """
        suffix = suffix.lower().lstrip(".")
        if not suffix:
            if raise_err:
                raise EmptySuffixError()
            return (cls.NOTYPE, tuple())

        matches = []
        for member in cls.get_filetypes():
            member_value = member.get_value()
            if member_value.extensions and suffix in member_value.extensions:
                if not return_matches:
                    return (member, tuple())
                matches.append(member)

        if len(matches) == 0:
            if raise_err:
                raise UnsupportedFileTypeError(
                    f"Unhandled filetype from suffix={suffix}"
                )
            return (cls.UNHANDLED, tuple())

        return (
            (matches[0], tuple())
            if not return_matches
            else (matches[0], tuple(matches))
        )

    @classmethod
    def from_mimetype(
        cls,
        file_path: Union[str, Path],
        raise_err: bool = False,
        return_matches: bool = False,
    ) -> Tuple[FileType, Tuple[FileType, ...]]:
        """Determines a filetype from a file's MIME type.

        Args:
            file_path (str): The path to the file.
            raise_err (bool, optional): Whether to raise an exception if the type is unhandled. Defaults to False.
            return_matches (bool, optional): Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

        Returns:
            FileType: The determined filetype enumeration member, or a tuple with the first matching filetype and a list of all options.

        Raises:
            FileNotFoundError: If the file does not exist.
            UnsupportedFileTypeError: If the file type is unhandled and raise_err is True.
        """
        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file_path)

        file_mimetype = guess_mime_type_from_file(str(file))

        matches = []
        for member in cls.get_filetypes():
            if (
                member.get_value().mime_types
                and file_mimetype in member.get_value().mime_types
            ):
                if not return_matches:
                    return (member, tuple())
                matches.append(member)

        if len(matches) == 0:
            if raise_err:
                raise UnsupportedFileTypeError(
                    f"Unhandled filetype from mimetype={file_mimetype}"
                )
            return (cls.UNHANDLED, tuple())

        return (
            (matches[0], tuple())
            if not return_matches
            else (matches[0], tuple(matches))
        )

    # @classmethod
    # def from_content(cls, path: Path, raise_err=False):
    #     file_path = Path(path)
    #     file_type = get_file_type(file_path)['f_type']
    #     # logger.info(file_type)
    #     return file_type #text/plain, application/json, text/xml, image/png, application/csv, image/gif, ...
    #     member = cls.UNHANDLED
    #     return member

    @classmethod
    def from_path(
        cls,
        path: Union[str, Path],
        read_content=False,
        raise_err=False,
        return_matches=False,
    ) -> Tuple[FileType, Tuple[FileType, ...]]:
        """Determines the filetype of a file based on its path. Optionally reads the file's content to verify its type.

        Args:
            path (Path): The path to the file.
            read_content (bool, optional): If True, the method also checks the file's content to determine its type.
                                           Defaults to False.
            raise_err (bool, optional): If True, raises exceptions for unsupported types or when file does not exist.
                                        Defaults to False.
            return_matches (bool, optional): Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

        Returns:
            FileType: The determined filetype enumeration member based on the file's suffix and/or content, or a tuple with the first matching filetype and a list of all options.

        Raises:
            FileNotFoundError: If the file does not exist when attempting to read its content.
            UnsupportedFileTypeError: If the file type is unsupported and raise_err is True.
            AssertionError: If there is a mismatch between the file type determined from the file's suffix and its content.
        """
        file_path = Path(path)

        raise_err_suffix: bool = raise_err and (not read_content)
        raise_err_mimetype: bool = raise_err

        # get member from suffix
        filetype_from_suffix, suffix_matches = cls.from_suffix(
            file_path.suffix, raise_err=raise_err_suffix, return_matches=True
        )

        # if we're not checking the file content, return
        if not read_content:
            return filetype_from_suffix, suffix_matches

        # the file should exist for content reading
        if not file_path.exists():
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        # get member from content
        filetype_from_mimetype, mimetype_matches = cls.from_mimetype(
            file_path, raise_err=raise_err_mimetype, return_matches=True
        )

        # combine results from both methods

        # if suffix didn't give a filetype, use the one from content
        if filetype_from_suffix.is_true_filetype():
            return (
                (filetype_from_suffix, tuple())
                if not return_matches
                else (filetype_from_mimetype, mimetype_matches)
            )

        # if content mimetype didn't give a filetype, use the one from suffix
        if filetype_from_mimetype.is_true_filetype():
            return (
                (filetype_from_suffix, tuple())
                if not return_matches
                else (filetype_from_suffix, suffix_matches)
            )

        # find common matches
        common_members = tuple(m for m in suffix_matches if m in mimetype_matches)

        if len(common_members) == 0:
            if raise_err:
                raise AssertionError(
                    f"file type from suffix ({suffix_matches}) mismatch with file type from content ({mimetype_matches})"
                )
            return (cls.NOTYPE, tuple())

        return (
            (common_members[0], tuple())
            if not return_matches
            else (common_members[0], common_members)
        )

    def is_true_filetype(self) -> bool:
        """Determines if the filetype instance represents a supported file type based on the presence of defined extensions.

        Returns:
            bool: True if the filetype has at least one associated file extension, False otherwise.
        """
        return len(self.get_value().extensions) != 0

    def get_one_suffix(self) -> str:
        """
        Retrieves the primary file extension associated with the filetype.

        Returns:
            str: The primary file extension for the filetype, prefixed with a period.
                 Returns an empty string if the filetype does not have an associated extension.
        """
        if not self.is_true_filetype():
            return ""
        ext = self.get_value().extensions[0]
        return f".{ext}"

    def get_one_mimetype(self) -> str:
        """
        Retrieves the primary mimetype associated with the filetype.

        Returns:
            Mimetype: The primary mimetype for the filetype.
                 Returns an empty string if the filetype does not have an associated extension.
        """
        if not self.is_true_filetype():
            return ""
        return self.get_value().mime_types[0]

    def is_valid_suffix(self, suffix: str, raise_err=False):
        """Validates whether a given file extension matches the filetype's expected extensions.

        Args:
            suffix (str): The file extension to validate, including the leading period (e.g., ".txt").
            raise_err (bool, optional): If True, raises a MismatchedException for invalid extensions.
                                        Defaults to False.

        Returns:
            bool: True if the suffix matches one of the filetype's extensions, False otherwise.

        Raises:
            MismatchedException: If the suffix does not match the filetype's extensions and raise_err is True.
        """
        if not self.is_true_filetype():
            return False
        suffix = self.__class__.clean_suffix(suffix)
        if suffix in self.get_value().extensions:
            return True
        if raise_err:
            raise MismatchedException(
                f"filetype ({self.name}) mismatch with suffix ({suffix})",
                suffix,
                self.get_one_suffix(),
            )
        return False

    def is_valid_path(
        self, file_path: Union[str, Path], read_content=False, raise_err=False
    ):
        """Validates the filetype of a given file path. Optionally reads the file's content to verify its type.

        Args:
            file_path (Union[str, Path]): The file path to validate.
            read_content (bool, optional): If True, the method also checks the file's content to validate its type.
                                           Defaults to False.
            raise_err (bool, optional): If True, raises exceptions for mismatched or unsupported types.
                                        Defaults to False.

        Returns:
            bool: True if the file path's type matches the filetype, False otherwise.

        Raises:
            AssertionError: If there is a mismatch between the file type determined from the file's suffix and its content.
            MismatchedException: If the file type determined from the file's suffix or content does not match the filetype.
        """
        _val, matches = self.from_path(
            file_path, read_content=read_content, return_matches=True
        )
        is_valid = (self == _val) if not self.is_true_filetype() else (self in matches)
        if raise_err and not is_valid:
            raise MismatchedException(
                f"suffix/mime-type ({file_path})", _val, self.get_value()
            )
        return is_valid

    def is_valid_mimetype(self, file_mimetype: str, raise_err=False):
        """Validates whether a given MIME type matches the filetype's expected MIME types.

        Args:
            file_mimetype (str): The MIME type to validate.
            raise_err (bool, optional): If True, raises a MismatchedException for invalid MIME types.
                                        Defaults to False.

        Returns:
            bool: True if the MIME type matches one of the filetype's MIME types, False otherwise.

        Raises:
            MismatchedException: If the MIME type does not match the filetype's MIME types and raise_err is True.
        """
        if not self.is_true_filetype():
            return False
        if file_mimetype in self.get_value().mime_types:
            return True
        if raise_err:
            raise MismatchedException(
                f"filetype ({self.name}) mismatch with mimetype ({file_mimetype})",
                self.get_one_mimetype(),
                file_mimetype,
            )
        return False

    def is_valid_mime_type(self, file_path: Path, raise_err=False):
        """
        Validates whether the MIME type of the file at the specified path aligns with the filetype's expected MIME types.

        This method first determines the filetype based on the file's actual MIME type (determined by reading the file's content)
        and then checks if this determined filetype matches the instance calling this method. Special consideration is given to
        filetype.TEXT, where a broader compatibility check is performed due to the generic nature of text MIME types.

        Args:
            file_path (Path): The path to the file whose MIME type is to be validated.
            raise_err (bool, optional): If True, a MismatchedException is raised if the file's MIME type does not match
                                        the expected MIME types of the filetype instance. Defaults to False.

        Returns:
            bool: True if the file's MIME type matches the expected MIME types for this filetype instance or if special
                compatibility conditions are met (e.g., for filetype.TEXT with "text/plain"). Otherwise, False.

        Raises:
            MismatchedException: If raise_err is True and the file's MIME type does not match the expected MIME types
                                for this filetype instance, including detailed information about the mismatch.
        """
        _val, matches = self.from_mimetype(file_path, return_matches=True)
        is_valid = (self == _val) if not self.is_true_filetype() else (self in matches)

        # many things can be text/plain
        if (self.TEXT in matches) and "text/plain" in self.get_value().upper_mime_types:
            is_valid = True

        if raise_err and not is_valid:
            raise MismatchedException(
                f"content-type({file_path})", _val, self.get_value().mime_types
            )
        return is_valid


def extract_enum_members(enum_cls: Type) -> Dict[str, MimeType]:
    """Extracts MimeType instances from an enum class.

    Args:
        enum_cls (Type): The enum class.

    Returns:
        Dict[str, MimeType]: Dictionary of MimeType instances keyed by enum member names.
    """
    extracted_members: Dict[str, MimeType] = {}
    items: Iterable

    if issubclass(enum_cls, FileType):
        enum_cls = enum_cls

    if issubclass(enum_cls, Enum):
        items = ((item.name, item.value) for item in enum_cls)
    else:
        assert hasattr(enum_cls, "__filetype_members__")
        filetype_members: Dict[str, MimeType] = enum_cls.__filetype_members__
        assert isinstance(filetype_members, dict)
        items = filetype_members.items()

    # Copy values from the added enum
    for item_name, item_value in items:
        # Make sure the value is of the inherited enum type
        assert isinstance(item_value, MimeType)
        extracted_members[item_name] = item_value

    return extracted_members


def extend_filetype_enum(added_enum: Type[Enum]) -> None:
    """Extends the BaseFileType enumeration with members from another enumeration.

    Args:
        added_enum (Type[Enum]): The enum class to extend BaseFileType with.
    """
    inherited_enum = FileType

    # Add new members from added_enum to inherited_enum
    for name, member in added_enum.__members__.items():
        extend_enum(inherited_enum, name, member.value)

    # Copy methods from inherited_enum and added_enum to the new class
    for method_name, method in {
        **added_enum.__dict__,
        **inherited_enum.__dict__,
    }.items():
        if callable(method) or isinstance(method, classmethod):
            setattr(inherited_enum, method_name, method)


class FileTypeExamples(Enum):
    """Enumeration of supported file types with methods for type determination and validation."""

    CSV = MimeType(("csv",), ("text/csv",), ("text/plain",))
    MARKDOWN = MimeType(("md",), ("text/markdown",), ("text/plain",))

    EXCEL = MimeType(
        ("xls", "xlsx"),
        (
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
    )
    MSWORD = MimeType(
        ("docx", "doc"),
        (
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/msword",
        ),
    )
    JSON = MimeType(("json",), ("application/json",))
    PDF = MimeType(("pdf",), ("application/pdf",))
    IMAGE = MimeType(("jpg", "jpeg", "png"), ("image/jpeg", "image/png"))
    GIF = MimeType(("gif",), ("image/gif",))
    VIDEO = MimeType(("mp4", "avi"), ("video/mp4", "video/x-msvideo"))
    XML = MimeType(("xml",), ("application/xml", "text/xml"))


extend_filetype_enum(FileTypeExamples)
