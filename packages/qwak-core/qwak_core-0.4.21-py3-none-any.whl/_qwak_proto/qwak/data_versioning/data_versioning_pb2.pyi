"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataTagSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    MODEL_ID_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    EXTENSION_TYPE_FIELD_NUMBER: builtins.int
    ENVIRONMENT_ID_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """The Build id - data saved in"""
    model_id: builtins.str
    """The model id - data saved in"""
    tag: builtins.str
    """Tag name data file is saved under"""
    extension_type: builtins.str
    """Extension file type"""
    environment_id: builtins.str
    """The environment the data is saved on"""
    path: builtins.str
    """The path we save the data in - it can be passed from outside in register"""
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
        model_id: builtins.str = ...,
        tag: builtins.str = ...,
        extension_type: builtins.str = ...,
        environment_id: builtins.str = ...,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_id", b"build_id", "environment_id", b"environment_id", "extension_type", b"extension_type", "model_id", b"model_id", "path", b"path", "tag", b"tag"]) -> None: ...

global___DataTagSpec = DataTagSpec

class DataTagFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_CONTAINS_FIELD_NUMBER: builtins.int
    TAG_PREFIX_FIELD_NUMBER: builtins.int
    tag_contains: builtins.str
    """Filter data tags by tag contains"""
    tag_prefix: builtins.str
    """Filter data tags by tag prefix"""
    def __init__(
        self,
        *,
        tag_contains: builtins.str = ...,
        tag_prefix: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter", "tag_contains", b"tag_contains", "tag_prefix", b"tag_prefix"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "tag_contains", b"tag_contains", "tag_prefix", b"tag_prefix"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["filter", b"filter"]) -> typing_extensions.Literal["tag_contains", "tag_prefix"] | None: ...

global___DataTagFilter = DataTagFilter
