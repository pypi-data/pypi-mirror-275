import logging
from typing import cast

import requests
from requests.compat import urljoin
from requests.exceptions import JSONDecodeError

from .settings import BASE_URL

logger = logging.getLogger(__name__)


def bc_authorize(
    client_id: str, client_secret: str, purpose: str, login_hint: str
) -> tuple[int, dict]:
    request_body = {
        'purpose': purpose,
        'login_hint': login_hint,
        'acr_values': 2
    }

    r = requests.post(
        urljoin(BASE_URL, 'bc-authorize'),
        data=request_body,
        auth=(client_id, client_secret),
        timeout=5
    )

    if r.status_code == 415:
        r = requests.post(
            urljoin(BASE_URL, 'bc-authorize'),
            json=request_body,
            auth=(client_id, client_secret),
            timeout=5
        )

    r.raise_for_status()

    return r.status_code, r.json()


def token(
    client_id: str, client_secret: str, auth_req_id: str, grant_type: str
) -> tuple[int, dict]:
    request_body = {'grant_type': grant_type, 'auth_req_id': auth_req_id}

    r = requests.post(
        urljoin(BASE_URL, 'token'),
        data=request_body,
        auth=(client_id, client_secret),
        timeout=5
    )

    if r.status_code == 415:
        r = requests.post(
            urljoin(BASE_URL, 'token'),
            json=request_body,
            auth=(client_id, client_secret),
            timeout=5
        )

    if not _is_auth_pending_error(r):
        r.raise_for_status()

    return r.status_code, r.json()


def post(
    endpoint: str, token_str: str, data: dict | None = None
) -> tuple[int, dict]:
    headers = {'Authorization': token_str}
    data = data or {}

    r = requests.post(
        endpoint,
        json=data,
        headers=headers,
        timeout=5
    )
    r.raise_for_status()

    return r.status_code, r.json()


def put(
    endpoint: str, token_str: str, data: dict | None = None
) -> tuple[int, dict]:
    headers = {'Authorization': token_str}
    data = data or {}

    r = requests.put(
        endpoint,
        json=data,
        headers=headers,
        timeout=5
    )
    r.raise_for_status()

    try:
        data = r.json()
    except JSONDecodeError:
        data = {}

    data = cast(dict, data)  # Help mypy typehints
    return r.status_code, data


def _is_auth_pending_error(response: requests.Response) -> bool:
    return (
        response.status_code == 400 and
        'error' in response.json() and
        response.json()['error'] == 'authorization_pending'
    )
