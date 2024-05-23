"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.priv.iam.v1.token.iam_token_pb2
import yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2
import yandex.cloud.priv.oauth.claims_pb2
import yandex.cloud.priv.oauth.v1.cloud_user_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AcceptEulaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COOKIE_HEADER_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    CLOUD_AGREEMENTS_FIELD_NUMBER: builtins.int
    cookie_header: builtins.str
    """HTTP-header Cookie with required authentication cookie values (e.g. Session_id)"""
    host: builtins.str
    """Service host address, for example "datalens.yandex.ru" or "tracker.yandex.com".
    Used for Yandex.Passport cookie validation (Yandex.Passport cookie is TLD-specific)
    """
    @property
    def cloud_agreements(self) -> global___YandexCloudAgreements: ...
    def __init__(
        self,
        *,
        cookie_header: builtins.str = ...,
        host: builtins.str = ...,
        cloud_agreements: global___YandexCloudAgreements | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cloud_agreements", b"cloud_agreements"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_agreements", b"cloud_agreements", "cookie_header", b"cookie_header", "host", b"host"]) -> None: ...

global___AcceptEulaRequest = AcceptEulaRequest

@typing.final
class AcceptEulaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_AGREEMENTS_FIELD_NUMBER: builtins.int
    @property
    def cloud_agreements(self) -> global___YandexCloudAgreements: ...
    def __init__(
        self,
        *,
        cloud_agreements: global___YandexCloudAgreements | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cloud_agreements", b"cloud_agreements"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_agreements", b"cloud_agreements"]) -> None: ...

global___AcceptEulaResponse = AcceptEulaResponse

@typing.final
class YandexCloudAgreements(google.protobuf.message.Message):
    """Yandex.Cloud agreements"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EULA_FIELD_NUMBER: builtins.int
    PRIVACY_POLICY_FIELD_NUMBER: builtins.int
    DENY_NOTIFICATIONS_FIELD_NUMBER: builtins.int
    eula: builtins.bool
    """current Yandex.Cloud EULA text is here https://yandex.ru/legal/cloud_termsofuse/"""
    privacy_policy: builtins.bool
    deny_notifications: builtins.bool
    """Deny receiving advertising and other informational messages from the company Yandex.Cloud LLC (OGRN 1187746678580)."""
    def __init__(
        self,
        *,
        eula: builtins.bool = ...,
        privacy_policy: builtins.bool = ...,
        deny_notifications: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deny_notifications", b"deny_notifications", "eula", b"eula", "privacy_policy", b"privacy_policy"]) -> None: ...

global___YandexCloudAgreements = YandexCloudAgreements

@typing.final
class CheckSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COOKIE_HEADER_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    FEDERATION_ID_FIELD_NUMBER: builtins.int
    cookie_header: builtins.str
    """HTTP-header Cookie with required per-service cookie values (e.g. yc_session)"""
    host: builtins.str
    """Service host address, for example "datalens.yandex.ru" or "tracker.yandex.com".
    Used for authorize_url TLD calculation, Yandex.Passport cookie revalidation (Yandex.Passport cookie is TLD-specific)
    """
    federation_id: builtins.str
    """If present - specified federation id should be used for authorization
    otherwise authorization IdP calculated from cookies.
    """
    def __init__(
        self,
        *,
        cookie_header: builtins.str = ...,
        host: builtins.str = ...,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cookie_header", b"cookie_header", "federation_id", b"federation_id", "host", b"host"]) -> None: ...

global___CheckSessionRequest = CheckSessionRequest

@typing.final
class CheckSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_CLAIMS_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    CLOUD_USER_INFO_FIELD_NUMBER: builtins.int
    IAM_TOKEN_FIELD_NUMBER: builtins.int
    PASSPORT_SESSION_FIELD_NUMBER: builtins.int
    @property
    def subject_claims(self) -> yandex.cloud.priv.oauth.claims_pb2.SubjectClaims:
        """Authenticated subject claims."""

    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """per-service cookie expiration time."""

    @property
    def cloud_user_info(self) -> yandex.cloud.priv.oauth.v1.cloud_user_pb2.CloudUserInfo: ...
    @property
    def iam_token(self) -> yandex.cloud.priv.iam.v1.token.iam_token_pb2.IamToken: ...
    @property
    def passport_session(self) -> global___PassportSession:
        """Yandex.Passport active multisession."""

    def __init__(
        self,
        *,
        subject_claims: yandex.cloud.priv.oauth.claims_pb2.SubjectClaims | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        cloud_user_info: yandex.cloud.priv.oauth.v1.cloud_user_pb2.CloudUserInfo | None = ...,
        iam_token: yandex.cloud.priv.iam.v1.token.iam_token_pb2.IamToken | None = ...,
        passport_session: global___PassportSession | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cloud_user_info", b"cloud_user_info", "expires_at", b"expires_at", "iam_token", b"iam_token", "passport_session", b"passport_session", "subject_claims", b"subject_claims"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_user_info", b"cloud_user_info", "expires_at", b"expires_at", "iam_token", b"iam_token", "passport_session", b"passport_session", "subject_claims", b"subject_claims"]) -> None: ...

global___CheckSessionResponse = CheckSessionResponse

@typing.final
class CheckPassportSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COOKIE_HEADER_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    cookie_header: builtins.str
    """HTTP-header Cookie with required per-service cookie values (e.g. yc_session)"""
    host: builtins.str
    """Service host address, for example "datalens.yandex.ru" or "tracker.yandex.com".
    Used for authorize_url TLD calculation, Yandex.Passport cookie revalidation (Yandex.Passport cookie is TLD-specific)
    """
    client_id: builtins.str
    """organization-manager.application ID that is used to authorize and issuer IAM-token"""
    def __init__(
        self,
        *,
        cookie_header: builtins.str = ...,
        host: builtins.str = ...,
        client_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "cookie_header", b"cookie_header", "host", b"host"]) -> None: ...

global___CheckPassportSessionRequest = CheckPassportSessionRequest

@typing.final
class CheckPassportSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_CLAIMS_FIELD_NUMBER: builtins.int
    IAM_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def subject_claims(self) -> yandex.cloud.priv.oauth.claims_pb2.SubjectClaims:
        """Authenticated subject claims."""

    @property
    def iam_token(self) -> yandex.cloud.priv.iam.v1.token.iam_token_pb2.IamToken: ...
    def __init__(
        self,
        *,
        subject_claims: yandex.cloud.priv.oauth.claims_pb2.SubjectClaims | None = ...,
        iam_token: yandex.cloud.priv.iam.v1.token.iam_token_pb2.IamToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["iam_token", b"iam_token", "subject_claims", b"subject_claims"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["iam_token", b"iam_token", "subject_claims", b"subject_claims"]) -> None: ...

global___CheckPassportSessionResponse = CheckPassportSessionResponse

@typing.final
class GetOpenIDConfigurationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    host: builtins.str
    def __init__(
        self,
        *,
        host: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host", b"host"]) -> None: ...

global___GetOpenIDConfigurationRequest = GetOpenIDConfigurationRequest

@typing.final
class GetOpenIDConfigurationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORIZATION_ENDPOINT_FIELD_NUMBER: builtins.int
    LOGOUT_ENDPOINT_FIELD_NUMBER: builtins.int
    TOKEN_ENDPOINT_FIELD_NUMBER: builtins.int
    USERINFO_ENDPOINT_FIELD_NUMBER: builtins.int
    REVOCATION_ENDPOINT_FIELD_NUMBER: builtins.int
    authorization_endpoint: builtins.str
    logout_endpoint: builtins.str
    token_endpoint: builtins.str
    userinfo_endpoint: builtins.str
    revocation_endpoint: builtins.str
    def __init__(
        self,
        *,
        authorization_endpoint: builtins.str = ...,
        logout_endpoint: builtins.str = ...,
        token_endpoint: builtins.str = ...,
        userinfo_endpoint: builtins.str = ...,
        revocation_endpoint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["authorization_endpoint", b"authorization_endpoint", "logout_endpoint", b"logout_endpoint", "revocation_endpoint", b"revocation_endpoint", "token_endpoint", b"token_endpoint", "userinfo_endpoint", b"userinfo_endpoint"]) -> None: ...

global___GetOpenIDConfigurationResponse = GetOpenIDConfigurationResponse

@typing.final
class PassportSession(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.oauth.claims_pb2.YandexClaims]:
        """Yandex.Passport active multisession user info (including default user)"""

    def __init__(
        self,
        *,
        users: collections.abc.Iterable[yandex.cloud.priv.oauth.claims_pb2.YandexClaims] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["users", b"users"]) -> None: ...

global___PassportSession = PassportSession

@typing.final
class CreateSessionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    COOKIE_HEADER_FIELD_NUMBER: builtins.int
    access_token: builtins.str
    """access_token from successful token response, see https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse for details."""
    domain: builtins.str
    """Which hosts are allowed to receive the cookie. In general - application should not send this parameter.
    Domain should match one of the client_id redirect_uri. Unmatched domain parameter is ignored.
    see http://www.rfcreader.com/#rfc6265_line474 for details.
    """
    cookie_header: builtins.str
    """HTTP-header Cookie with optional per-service cookie values (e.g. yc_device)"""
    def __init__(
        self,
        *,
        access_token: builtins.str = ...,
        domain: builtins.str = ...,
        cookie_header: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["access_token", b"access_token", "cookie_header", b"cookie_header", "domain", b"domain"]) -> None: ...

global___CreateSessionRequest = CreateSessionRequest

@typing.final
class CreateSessionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SET_COOKIE_HEADER_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    @property
    def set_cookie_header(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """HTTP-header Set-Cookie for End-User with required per-service cookies, e.g. yc_session"""

    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """per-service cookie expiration time."""

    def __init__(
        self,
        *,
        set_cookie_header: collections.abc.Iterable[builtins.str] | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["expires_at", b"expires_at", "set_cookie_header", b"set_cookie_header"]) -> None: ...

global___CreateSessionResponse = CreateSessionResponse

@typing.final
class LogoutRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COOKIE_HEADER_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    cookie_header: builtins.str
    """HTTP-header Cookie with required per-service cookie values (e.g. yc_session)"""
    domain: builtins.str
    """Which hosts are allowed to receive the cookie. In general - application should not send this parameter.
    Domain should match one of the client_id redirect_uri. Unmatched domain parameter is ignored.
    see http://www.rfcreader.com/#rfc6265_line474 for details.
    """
    def __init__(
        self,
        *,
        cookie_header: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cookie_header", b"cookie_header", "domain", b"domain"]) -> None: ...

global___LogoutRequest = LogoutRequest

@typing.final
class LogoutResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_FIELD_NUMBER: builtins.int
    SET_COOKIE_HEADER_FIELD_NUMBER: builtins.int
    SUBJECT_CLAIMS_FIELD_NUMBER: builtins.int
    @property
    def subject(self) -> yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2.Subject: ...
    @property
    def set_cookie_header(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """HTTP-header Set-Cookie for End-User with required per-service cookies, e.g. yc_session
        Cloud-specific user authentication cookies should be removed by Set-Cookie header.
        """

    @property
    def subject_claims(self) -> yandex.cloud.priv.oauth.claims_pb2.SubjectClaims:
        """minimal subject claims"""

    def __init__(
        self,
        *,
        subject: yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2.Subject | None = ...,
        set_cookie_header: collections.abc.Iterable[builtins.str] | None = ...,
        subject_claims: yandex.cloud.priv.oauth.claims_pb2.SubjectClaims | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["subject", b"subject", "subject_claims", b"subject_claims"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["set_cookie_header", b"set_cookie_header", "subject", b"subject", "subject_claims", b"subject_claims"]) -> None: ...

global___LogoutResponse = LogoutResponse

@typing.final
class AuthorizationRequired(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORIZE_URL_FIELD_NUMBER: builtins.int
    authorize_url: builtins.str
    """authorize URL, e.g. URL for /authorize OpenID Connect endpoint."""
    def __init__(
        self,
        *,
        authorize_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["authorize_url", b"authorize_url"]) -> None: ...

global___AuthorizationRequired = AuthorizationRequired
