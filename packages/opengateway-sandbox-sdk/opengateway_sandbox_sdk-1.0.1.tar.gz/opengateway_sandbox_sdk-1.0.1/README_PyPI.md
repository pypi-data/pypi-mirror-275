# Opengateway-Sandbox-SDK

Welcome to Telefonica's Sandbox SDK, a secure environment where you can try out and test our network APIs, validate your own use cases or develop new experiences for your customers.

## SIM Swap
### Introduction
In the next sample we will check if the network has detected a SIM swap, as a safety measure before doing an important action. This can help preventing impersonation of our users.

To that effect, we will use SIM Swap API. SIM Swap offers the ability to check when the last SIM swap was produced and return if it was produced after a threshold.

### Code
#### Client creation
First step is to instantiate the class Simswap from the corresponding SDK. We will need the credentials and the phone number of the user.

```Python
from sandbox.opengatewaysdk import Simswap
 
phone_number = get_user_phone_number()

simswap_client = Simswap('your-client-id', 'your-client-secret', phone_number) 
```

#### Usage
Then we use the SDK in order to check if a sim swap was detected in the last "max_age" hours.

```Python
max_age = 100
simswap_client.check(max_age)
Or you can get the moment where the las SIM Swap was performed.

simswap_client.retrieve_date()
```

### Details

- SimSwap(client_id: str, client_secret: str, phone_number: str):
  - Class constructor
  - client_id (str): ClientID from Developer Hub - Sandbox
  - client_secret (str): Client secret from Developer Hub - Sandbox
  - phone_number (str): Phone Number to check SIM Swap status. Example: '+346xxxxxxxx'
- SimSwap.check(self, max_age:int) → bool:
  - max_age (int): Period in hours to be checked for SIM Swap
  - Returns bool, true if the SIM was swapped during the "max_age" period
- SimSwap.retrieve_date(self) → datetime:
  - Returns datetime.datetime with the Timestamp of latest SIM swap performed

## Qod home devices
### Introduction
In the next sample we will improve the quality of service for a device in our home WiFi for real time apps.

To that effect, we will use QoDHome API. QoDHome offers the ability to control all the devices connected to the user's home network.

### Code
#### Client creation
First step is to instantiate the class QoDHome from the corresponding SDK. We will need the credentials and public IP of the user.

```Python
from sandbox.opengatewaysdk.qodhome import QoDHome, ServiceClass
 
public_ip = get_user_public_ip()
 
qod_client = QoDHome('your-client-id', 'your-client-secret', public_ip)
```

#### Usage
Then we use the SDK in order to set the quality of service to the device, using the local IP of the device.

```Python
local_ip = get_local_ip()
 
# One line Open Gateway query
result = qod_client.qos(local_ip, ServiceClass.RealTimeInteractive)
```

### Details
- QoDHome(client_id: str, client_secret: str, public_ip: str):
  - Class constructor
  - client_id (str): ClientID from Developer Hub - Sandbox
  - client_secret (str): Client secret from Developer Hub - Sandbox
  - public_ip (str): External IP of the device.
- QoDHome.qos(self, internal_ip: str, service_class: ServiceClass) -> bool:
  - internal_ip (str): Internal IP address of the connected device in the LAN.
  - service_class (ServiceClass): Service class to prioritize
  - Returns true if the operation has been carried out successfully


- ServiceClass
  - The name of the service class requested by the API client. It is associated with QoS behaviors optimised for a particular application type.
  - Enum of the available application types:
    - REALTIMEINTERACTIVE = 'real_time_interactive'
    - MULTIMEDIASTREAMING = 'multimedia_streaming'
    - BROADCASTVIDEO = 'broadcast_video'
    - LOWLATENCYDATA = 'low_latency_data'
    - HIGHTHROUGHPUTDATA = 'high_throughput_data'
    - LOWPRIORITYDATA = 'low_priority_data'
    - STANDARD = 'standard'

Application examples of the different service class:

| Service Class Name    | Application Examples                          |
|-----------------------|-----------------------------------------------|
| Standard              | Undifferentiated applications                 |
| Real-Time Interactive | Video conferencing and Interactive gaming     |
| Multimedia Streaming  | Streaming video and audio on demand           |
| Low-Priority Data     | Any flow that has no BW assurance             |
| Low-Latency Data      | Client/server transactions Web-based ordering |
| High-Throughput Data  | Store and forward applications                |
| Broadcast Video       | Broadcast TV & live events                    |
