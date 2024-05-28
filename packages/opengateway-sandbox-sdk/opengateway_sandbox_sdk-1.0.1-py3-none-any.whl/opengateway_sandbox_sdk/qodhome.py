from enum import Enum

from . import httpclient
from .clientcredentials import ClientSecretApikey
from .purposes import QoDHomePurpose
from .settings import BASE_URL


class ServiceClass(str, Enum):
    REAL_TIME_INTERACTIVE = 'real_time_interactive'
    MULTIMEDIA_STREAMING = 'multimedia_streaming'
    BROADCAST_VIDEO = 'broadcast_video'
    LOW_LATENCY_DATA = 'low_latency_data'
    HIGH_THROUGHPUT_DATA = 'high_throughput_data'
    LOW_PRIORITY_DATA = 'low_priority_data'
    STANDARD = 'standard'


class QoDHome:  # pylint: disable=too-few-public-methods
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        public_ip: str,
        purpose: QoDHomePurpose = QoDHomePurpose.REQUESTED_SERVICE_PROVISION
    ):
        self.public_ip = public_ip
        self.credentials = ClientSecretApikey(
            client_id,
            client_secret,
            'ip:'+public_ip,
            purpose.value
        )
        self.base_url = BASE_URL + 'home-devices-qod/v0/qos'

    def qos(self, internal_ip: str, service_class: ServiceClass) -> bool:
        token = self.credentials.get_token()
        data = {
            'serviceClass': service_class.value,
            'ipAddress': internal_ip
        }

        status, _ = httpclient.put(
            endpoint=self.base_url, token_str=token, data=data
        )

        return status == 204
