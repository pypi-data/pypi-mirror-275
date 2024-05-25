import base64
import json
import typing
from dataclasses import dataclass
from enum import StrEnum
from urllib.parse import urljoin

import requests
from requests.exceptions import JSONDecodeError

from pkgs.argument_parser import CachedParser
from pkgs.serialization_util import serialize_for_api
from pkgs.serialization_util.serialization_helpers import JsonValue
from uncountable.types.client_base import APIRequest, ClientMethods

from .file_upload import FileUpload, FileUploader, UploadedFile
from .types import AuthDetails, AuthDetailsApiKey

DT = typing.TypeVar("DT")


class EndpointMethod(StrEnum):
    POST = "POST"
    GET = "GET"


@dataclass(kw_only=True)
class HTTPRequestBase:
    method: EndpointMethod
    url: str
    headers: dict[str, str]
    body: typing.Optional[typing.Union[str, dict[str, str]]] = None
    query_params: typing.Optional[dict[str, str]] = None


@dataclass(kw_only=True)
class HTTPGetRequest(HTTPRequestBase):
    method: typing.Literal[EndpointMethod.GET]
    query_params: dict[str, str]


@dataclass(kw_only=True)
class HTTPPostRequest(HTTPRequestBase):
    method: typing.Literal[EndpointMethod.POST]
    body: typing.Union[str, dict[str, str]]


HTTPRequest = HTTPPostRequest | HTTPGetRequest



@dataclass(kw_only=True)
class ClientConfig():
    allow_insecure_tls: bool = False
      

class APIResponseError(BaseException):
    status_code: int
    message: str
    extra_details: dict[str, JsonValue] | None

    def __init__(
        self, status_code: int, message: str, extra_details: dict[str, JsonValue] | None
    ) -> None:
        super().__init__(status_code, message, extra_details)
        self.status_code = status_code
        self.message = message
        self.extra_details = extra_details

    @classmethod
    def construct_error(
        cls, status_code: int, extra_details: dict[str, JsonValue] | None
    ) -> "APIResponseError":
        message: str
        match status_code:
            case 403:
                message = "unexpected: unauthorized"
            case 410:
                message = "unexpected: not found"
            case 400:
                message = "unexpected: bad arguments"
            case 501:
                message = "unexpected: unimplemented"
            case 504:
                message = "unexpected: timeout"
            case 404:
                message = "not found"
            case 409:
                message = "bad arguments"
            case 422:
                message = "unprocessable"
            case _:
                message = "unknown error"
        return APIResponseError(
            status_code=status_code, message=message, extra_details=extra_details
        )


class SDKError(BaseException):
    message: str

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"internal SDK error, please contact Uncountable support: {self.message}"


class Client(ClientMethods):
    _parser_map: dict[type, CachedParser] = {}
    _auth_details: AuthDetails
    _base_url: str
    _file_uploader: FileUploader
    _cfg: ClientConfig

    def __init__(self, *, base_url: str, auth_details: AuthDetails, config: ClientConfig | None = None):
        self._auth_details = auth_details
        self._base_url = base_url
        self._file_uploader = FileUploader(self._base_url, self._auth_details)
        self._cfg = config or ClientConfig()

    def do_request(self, *, api_request: APIRequest, return_type: type[DT]) -> DT:
        http_request = self._build_http_request(api_request=api_request)
        match http_request:
            case HTTPGetRequest():
                response = requests.get(
                    http_request.url,
                    headers=http_request.headers,
                    params=http_request.query_params,
                    verify=not self._cfg.allow_insecure_tls
                )
            case HTTPPostRequest():
                response = requests.post(
                    http_request.url,
                    headers=http_request.headers,
                    data=http_request.body,
                    params=http_request.query_params,
                    verify=not self._cfg.allow_insecure_tls
                )
            case _:
                typing.assert_never(http_request)
        if response.status_code < 200 or response.status_code > 299:
            extra_details: dict[str, JsonValue] | None = None
            try:
                data = response.json()
                if "error" in data:
                    extra_details = data["error"]
            except JSONDecodeError:
                pass
            raise APIResponseError.construct_error(
                status_code=response.status_code, extra_details=extra_details
            )
        cached_parser = self._get_cached_parser(return_type)
        try:
            data = response.json()["data"]
            return cached_parser.parse_api(data)
        except ValueError | JSONDecodeError:
            raise SDKError("unable to process response")

    def _get_cached_parser(self, data_type: type[DT]) -> CachedParser[DT]:
        if data_type not in self._parser_map:
            self._parser_map[data_type] = CachedParser(data_type)
        return self._parser_map[data_type]

    def _build_auth_headers(self) -> dict[str, str]:
        match self._auth_details:
            case AuthDetailsApiKey():
                encoded = base64.standard_b64encode(
                    f"{self._auth_details.api_id}:{self._auth_details.api_secret_key}".encode()
                ).decode("utf-8")
                return {"Authorization": f"Basic {encoded}"}
        typing.assert_never(self._auth_details)

    def _build_http_request(self, *, api_request: APIRequest) -> HTTPRequest:
        headers = self._build_auth_headers()
        method = api_request.method.lower()
        data = {"data": json.dumps(serialize_for_api(api_request.args))}
        match method:
            case "get":
                return HTTPGetRequest(
                    method=EndpointMethod.GET,
                    url=urljoin(self._base_url, api_request.endpoint),
                    query_params=data,
                    headers=headers,
                )
            case "post":
                return HTTPPostRequest(
                    method=EndpointMethod.POST,
                    url=urljoin(self._base_url, api_request.endpoint),
                    body=data,
                    headers=headers,
                )
            case _:
                raise ValueError(f"unsupported request method: {method}")

    def upload_files(
        self: typing.Self, *, file_uploads: list[FileUpload]
    ) -> list[UploadedFile]:
        """Upload files to uncountable, returning file ids that are usable with other SDK operations."""
        return self._file_uploader.upload_files(file_uploads=file_uploads)
