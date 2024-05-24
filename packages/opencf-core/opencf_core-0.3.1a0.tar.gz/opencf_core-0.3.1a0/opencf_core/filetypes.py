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
- filetype: Enum class that encapsulates various file types supported by the system, providing methods for
            type determination from file attributes.

Functions:
- test_file_type_parsing(): Demonstrates and validates the parsing functionality for various file types.
- test_file_type_matching(): Tests the matching and validation capabilities of the filetype class.

Dependencies:
- collections.namedtuple: For defining simple classes for storing MIME type information.
- enum.Enum: For creating the filetype enumeration.
- pathlib.Path: For file path manipulations and checks.
- opencf_core.mimes.guess_mime_type_from_file: Utility function to guess MIME type from a file path.
"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum, EnumMeta
from pathlib import Path
from typing import Callable, Dict, Iterable, Tuple, Type, Union

from opencf_core.exceptions import (
    EmptySuffixError,
    MismatchedException,
    UnsupportedFileTypeError,
)

from .mimes import guess_mime_type_from_file


# File Type and MIME Type Definitions
@dataclass(eq=False, frozen=True)
class MimeType:
    extensions: Tuple[str, ...] = ()
    mime_types: Tuple[str, ...] = ()
    upper_mime_types: Tuple[str, ...] = ()


class BaseFileType(ABCMeta, EnumMeta):  # type:ignore
    NOTYPE: MimeType = MimeType()
    TEXT = MimeType(("txt",), ("text/plain",))
    UNHANDLED: MimeType = MimeType()

    __filetype_members__ = {"NOTYPE": NOTYPE, "TEXT": TEXT, "UNHANDLED": UNHANDLED}

    @abstractmethod
    def get_value(self) -> MimeType:
        pass

    @classmethod
    def from_mimetype(cls, file_path: Union[str, Path], raise_err: bool = False):
        pass

    @classmethod
    def from_path(cls, path: Path, read_content=False, raise_err=False):
        pass

    @classmethod
    def from_suffix(cls, suffix: str, raise_err: bool = False):
        pass

    @abstractmethod
    def is_true_filetype(self) -> bool:
        pass

    @abstractmethod
    def get_suffix(self) -> str:
        pass


class FileTypeMethods(BaseFileType):
    def get_value(self) -> MimeType:
        # self.value is defined for Enum subclass instances
        return self.value  # type:ignore

    @classmethod
    def get_filetypes(cls):
        for member in cls:
            if not isinstance(member.get_value(), MimeType):
                continue
            yield member

    @classmethod
    def from_suffix(cls, suffix: str, raise_err: bool = False):
        """
        Determines a filetype from a file's suffix.

        Args:
            suffix (str): The file suffix (extension).
            raise_err (bool, optional): Whether to raise an exception if the type is unhandled. Defaults to False.

        Returns:
            filetype: The determined filetype enumeration member.

        Raises:
            EmptySuffixError: If the suffix is empty and raise_err is True.
            UnsupportedFileTypeError: If the file type is unhandled and raise_err is True.
        """

        # get suffix
        suffix = suffix.lower().lstrip(".")
        if not suffix:
            if raise_err:
                raise EmptySuffixError()
            return cls.NOTYPE

        # get a valid member
        for member in cls.get_filetypes():
            member_value = member.get_value()
            if member_value.extensions and suffix in member_value.extensions:
                return member

        if raise_err:
            raise UnsupportedFileTypeError(f"Unhandled filetype from suffix={suffix}")

        return cls.UNHANDLED

    @classmethod
    def from_mimetype(cls, file_path: Union[str, Path], raise_err: bool = False):
        """
        Determines a filetype from a file's MIME type.

        Args:
            file_path (str): The path to the file.
            raise_err (bool, optional): Whether to raise an exception if the type is unhandled. Defaults to False.

        Returns:
            filetype: The determined filetype enumeration member.

        Raises:
            FileNotFoundError: If the file does not exist.
            UnsupportedFileTypeError: If the file type is unhandled and raise_err is True.
        """

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file_path)

        file_mimetype = guess_mime_type_from_file(str(file))

        for member in cls.get_filetypes():
            if (
                member.get_value().mime_types
                and file_mimetype in member.get_value().mime_types
            ):
                return member

        if raise_err:
            raise UnsupportedFileTypeError(
                f"Unhandled filetype from mimetype={file_mimetype}"
            )
        else:
            return cls.UNHANDLED

    # @classmethod
    # def from_content(cls, path: Path, raise_err=False):
    #     file_path = Path(path)
    #     file_type = get_file_type(file_path)['f_type']
    #     # logger.info(file_type)
    #     return file_type #text/plain, application/json, text/xml, image/png, application/csv, image/gif, ...
    #     member = cls.UNHANDLED
    #     return member

    @classmethod
    def from_path(cls, path: Path, read_content=False, raise_err=False):
        """
        Determines the filetype of a file based on its path. Optionally reads the file's content to verify its type.

        Args:
            path (Path): The path to the file.
            read_content (bool, optional): If True, the method also checks the file's content to determine its type.
                                           Defaults to False.
            raise_err (bool, optional): If True, raises exceptions for unsupported types or when file does not exist.
                                        Defaults to False.

        Returns:
            filetype: The determined filetype enumeration member based on the file's suffix and/or content.

        Raises:
            FileNotFoundError: If the file does not exist when attempting to read its content.
            UnsupportedFileTypeError: If the file type is unsupported and raise_err is True.
            AssertionError: If there is a mismatch between the file type determined from the file's suffix and its content.
        """
        file_path = Path(path)

        raise_err1 = raise_err and (not read_content)
        raise_err2 = raise_err

        # get member from suffix
        member1 = cls.from_suffix(file_path.suffix, raise_err=raise_err1)

        # if we're not checking the file content, return
        if not read_content:
            return member1

        # the file should exists for content reading
        if not file_path.exists():
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        # get member from content
        member2 = cls.from_mimetype(file_path, raise_err=raise_err2)

        # if suffix didnt give a filetype, use the one from content
        if not member1.is_true_filetype():
            return member2

        assert (
            member1 == member2
        ), f"file type from suffix ({member1}) mismatch with filepath from path({member2})"

        return member1

    def is_true_filetype(self) -> bool:
        """
        Determines if the filetype instance represents a supported file type based on the presence of defined extensions.

        Returns:
            bool: True if the filetype has at least one associated file extension, False otherwise.
        """
        return len(self.get_value().extensions) != 0

    def get_suffix(self) -> str:
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

    def is_valid_suffix(self, suffix: str, raise_err=False):
        """
        Validates whether a given file extension matches the filetype's expected extensions.

        Args:
            suffix (str): The file extension to validate, including the leading period (e.g., ".txt").
            raise_err (bool, optional): If True, raises a MismatchedException for invalid extensions.
                                        Defaults to False.

        Returns:
            bool: True if the suffix matches one of the filetype's extensions, False otherwise.

        Raises:
            MismatchedException: If the suffix does not match and raise_err is True.
        """
        _val = self.from_suffix(suffix=suffix)
        is_valid = _val == self
        if raise_err and not is_valid:
            raise MismatchedException(
                f"suffix ({suffix})", _val, self.get_value().extensions
            )
        return is_valid

    def is_valid_path(self, path: Path, raise_err=False, read_content=False):
        """
        Validates whether the file at a given path matches the filetype, optionally checking the file's content.

        Args:
            path (Path): The path to the file to validate.
            raise_err (bool, optional): If True, raises a MismatchedException for a mismatching file type.
                                        Defaults to False.
            read_content (bool, optional): If True, also validates the file's content type against the filetype.
                                           Defaults to False.

        Returns:
            bool: True if the file's type matches the filetype, based on its path and optionally its content.
                  False otherwise.

        Raises:
            MismatchedException: If the file's type does not match and raise_err is True.
        """
        _val = self.from_path(path, read_content=read_content)
        is_valid = _val == self
        if raise_err and not is_valid:
            raise MismatchedException(
                f"suffix/mime-type ({path})", _val, self.get_value()
            )
        return is_valid

    def is_valid_mime_type(self, path: Path, raise_err=False):
        """
        Validates whether the MIME type of the file at the specified path aligns with the filetype's expected MIME types.

        This method first determines the filetype based on the file's actual MIME type (determined by reading the file's content)
        and then checks if this determined filetype matches the instance calling this method. Special consideration is given to
        filetype.TEXT, where a broader compatibility check is performed due to the generic nature of text MIME types.

        Args:
            path (Path): The path to the file whose MIME type is to be validated.
            raise_err (bool, optional): If True, a MismatchedException is raised if the file's MIME type does not match
                                        the expected MIME types of the filetype instance. Defaults to False.

        Returns:
            bool: True if the file's MIME type matches the expected MIME types for this filetype instance or if special
                compatibility conditions are met (e.g., for filetype.TEXT with "text/plain"). Otherwise, False.

        Raises:
            MismatchedException: If raise_err is True and the file's MIME type does not match the expected MIME types
                                for this filetype instance, including detailed information about the mismatch.
        """
        _val = self.from_mimetype(path)
        is_valid = _val == self

        # many things can be text/plain
        if _val == self.TEXT and "text/plain" in self.get_value().upper_mime_types:
            is_valid = True

        if raise_err and not is_valid:
            raise MismatchedException(
                f"content-type({path})", _val, self.get_value().mime_types
            )
        return is_valid


def dd(cls: Type):
    joined: Dict[str, MimeType] = {}
    items: Iterable

    # Copy values from the inherited enum
    if issubclass(cls, Enum):
        items = ((item.name, item.value) for item in cls)
    else:
        assert hasattr(cls, "__filetype_members__")
        filetype_members: Dict[str, MimeType] = cls.__filetype_members__
        assert isinstance(filetype_members, dict)
        items = filetype_members.items()

    # Copy values from the added enum
    for item_name, item_value in items:
        # Make sure the value is of the inherited enum type
        assert isinstance(item_value, MimeType)
        joined[item_name] = item_value

    return joined


def extend_filetype_enum(
    inherited_enum: Union[Type[Enum], Type[BaseFileType]],
) -> Callable[[Union[Type[Enum], Type[BaseFileType]]], Type[Enum]]:
    def wrapper(added_enum: Union[Type[Enum], Type[BaseFileType]]) -> Type[Enum]:
        # Create a dictionary to hold the merged enum values
        joined = {}

        joined.update(dd(inherited_enum))
        joined.update(dd(added_enum))

        # Create a new Enum class with the merged values$
        new_enum = Enum(added_enum.__name__, joined)  # type: ignore

        # users can override/add enum members, methods, class methods in the added enum
        methods = tuple(inherited_enum.__dict__.items()) + tuple(
            added_enum.__dict__.items()
        )

        # Copy methods and class methods from the inherited enum
        for method_name, method in methods:
            if callable(method):
                setattr(new_enum, method_name, method)
            if isinstance(method, classmethod):
                setattr(new_enum, method_name, method)

        return new_enum

    return wrapper


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


# add an enum that contains members
# it does need to be an enum but it is easier to define members in a Enum subclass
# than using __filetype_members__ to list predifined mimetypes
@extend_filetype_enum(FileTypeExamples)
# add an subclass of BaseFileType that implements methods i use in other modules,
# on instances of mixin(FileTypeExamples, FileTypeMethods) (like FileType)
@extend_filetype_enum(FileTypeMethods)
class FileType(FileTypeMethods):
    # __filetype_members__: Dict[str, MimeType] = {}
    pass
