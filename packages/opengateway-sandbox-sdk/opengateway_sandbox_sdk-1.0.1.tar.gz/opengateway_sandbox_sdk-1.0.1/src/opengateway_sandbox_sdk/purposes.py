from enum import Enum


class QoDHomePurpose(str, Enum):
    REQUESTED_SERVICE_PROVISION = (
        'dpv:RequestedServiceProvision#home-devices-qod'
    )


class SimswapPurpose(str, Enum):
    FRAUD_PREVENTION_AND_DETECTION = 'dpv:FraudPreventionAndDetection#sim-swap'
