"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class NodeExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NODE_ID_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder that will be matched with Node ACL."""
    node_id: builtins.str
    """ID of the Node to perform request on."""
    @property
    def input(self) -> google.protobuf.struct_pb2.Struct:
        """Input data for the execution."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        node_id: builtins.str = ...,
        input: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["input", b"input"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "input", b"input", "node_id", b"node_id"]) -> None: ...

global___NodeExecutionRequest = NodeExecutionRequest

@typing.final
class NodeExecutionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPUT_FIELD_NUMBER: builtins.int
    @property
    def output(self) -> google.protobuf.struct_pb2.Struct:
        """Result of the execution."""

    def __init__(
        self,
        *,
        output: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["output", b"output"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["output", b"output"]) -> None: ...

global___NodeExecutionResponse = NodeExecutionResponse

@typing.final
class AliasExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    ALIAS_NAME_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder that will be matched with Alias ACL"""
    alias_name: builtins.str
    """Name of the Alias to perform request on"""
    @property
    def input(self) -> google.protobuf.struct_pb2.Struct:
        """Input data for the execution"""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        alias_name: builtins.str = ...,
        input: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["input", b"input"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["alias_name", b"alias_name", "folder_id", b"folder_id", "input", b"input"]) -> None: ...

global___AliasExecutionRequest = AliasExecutionRequest

@typing.final
class AliasExecutionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPUT_FIELD_NUMBER: builtins.int
    @property
    def output(self) -> google.protobuf.struct_pb2.Struct:
        """Result of the execution"""

    def __init__(
        self,
        *,
        output: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["output", b"output"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["output", b"output"]) -> None: ...

global___AliasExecutionResponse = AliasExecutionResponse
