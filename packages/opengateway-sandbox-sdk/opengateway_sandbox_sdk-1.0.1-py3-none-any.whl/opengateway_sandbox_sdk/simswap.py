from datetime import datetime

from .clientcredentials import ClientSecretApikey, httpclient
from .purposes import SimswapPurpose
from .settings import BASE_URL


class Simswap:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        phone_number: str,
        purpose: SimswapPurpose = SimswapPurpose.FRAUD_PREVENTION_AND_DETECTION
    ):
        self.phone_number = phone_number
        self.credentials = ClientSecretApikey(
            client_id,
            client_secret,
            'phone_number:'+phone_number,
            purpose.value
        )
        self.base_url = BASE_URL + 'sim-swap/v0/'

    def retrieve_date(self) -> datetime:
        token = self.credentials.get_token()
        data = {
            'phoneNumber': self.phone_number
        }

        _, json = httpclient.post(
            endpoint=self.base_url+'retrieve-date', token_str=token, data=data
        )

        return datetime.fromisoformat(
            json['latestSimChange'].partition('Z')[0]
        )

    def check(self, max_age: int) -> bool:
        token = self.credentials.get_token()
        data = {
            'phoneNumber': self.phone_number,
            'maxAge': max_age
        }
        _, json = httpclient.post(
            endpoint=self.base_url+'check', token_str=token, data=data
        )

        return json['swapped']
