# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
import time

from . import httpclient
from .settings import GRANT_TYPE

MAX_TRIES = 5


class ClientCredentials:
    def get_token(self) -> str:
        raise NotImplementedError


class ClientSecretApikey(ClientCredentials):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        login_hint: str,
        purpose: str
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.login_hint = login_hint
        self.grant_type = GRANT_TYPE
        self.purpose = purpose
        self._auth_req_id = ''
        self._interval = 0
        self._consent_url = ''
        self._token = ''
        self._token_type = ''
        self._get_auth()

    def _post_bc_authorize(self) -> None:
        status, response = httpclient.bc_authorize(
            self.client_id,
            self.client_secret,
            self.purpose,
            self.login_hint
        )
        if status == 200:
            self._auth_req_id = response['auth_req_id']
            self._interval = response.get('interval', None)
            self._consent_url = response.get('consent_url', None)

        if self._consent_url:
            raise ValueError(f'Send your user to {self._consent_url}')

    def _post_token(self) -> None:
        status, response = httpclient.token(
            self.client_id,
            self.client_secret,
            self._auth_req_id,
            self.grant_type
        )
        num_try = 0

        while status == 400 and num_try < MAX_TRIES:
            time.sleep(self._interval)
            num_try += 1
            status, response = httpclient.token(
                self.client_id,
                self.client_secret,
                self._auth_req_id,
                self.grant_type
            )

        if status == 200:
            self._token = response['access_token']
            self._token_type = response['token_type']
        else:
            raise ValueError(f'Could not get token after {MAX_TRIES} retries')

    def _get_auth(self) -> None:
        self._post_bc_authorize()
        self._post_token()

    def get_token(self) -> str:
        return ' '.join([self._token_type, self._token])
