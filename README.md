# Proofpoint Security Awareness Training API Package

Library implements all of the functions of the TAP API via Python.

### Requirements:

* Python 3.9+
* requests
* pysocks

### Installing the Package

You can install the API library using the following command directly from Github.

```
pip install git+https://github.com/pfptcommunity/tap-python.git
```

or can install the API library using pip.

```
pip install tap-api
```

### TAP API Versions

Selecting the version of the TAP API is done at time of import.

```python
# Version v0.3.0 
from tap_api.v2 import *
```

### Creating an API client object

```python
from tap_api.v2 import *

if __name__ == '__main__':
    client = Client("<principal>","<secret>")
```


### Querying VAP Data

```python
if __name__ == '__main__':
    client = Client("<principal>","<secret>")
    vap_info = client.people.vap()

    print("HTTP Status:", vap_info.get_status())
    print("HTTP Reason:", vap_info.get_reason())
    print("Total VAPs:", vap_info.total_vap_users)
    print("Interval:", vap_info.interval)
    print("Average Attack Index:", vap_info.average_attack_index)
    print("VAP Attack Threshold:", vap_info.vap_attack_index_threshold)

    for user in vap_info.users:
        identity = user.identity
        threat_statistics = user.threat_statistics

        print("\nUser Details:")
        print("  Email(s):", identity.emails)
        print("  Name:", identity.name or "N/A")
        print("  Department:", identity.department or "N/A")
        print("  Location:", identity.location or "N/A")
        print("  Title:", identity.title or "N/A")
        print("  VIP:", identity.vip)

        print("Threat Statistics:")
        print("  Attack Index:", threat_statistics.attack_index)
        print("  Threat Families:")
        for family in threat_statistics.families:
            print(f"    - {family.name}: {family.score}")
```

### Proxy Support

Socks5 Proxy Example:

```python
from tap_api.v2 import *

if __name__ == '__main__':
    client = Client("<principal>","<secret>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('socks5', credentials, '<your_proxy>', '8128')}
```

HTTP Proxy Example (Squid):

```python
from tap_api.v3 import *

if __name__ == '__main__':
    client = Client("<principal>","<secret>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('http', credentials, '<your_proxy>', '3128')}

```

### HTTP Timeout Settings

```python
from tap_api.v3 import *

if __name__ == '__main__':
    client = Client("<principal>","<secret>")
    # Timeout in seconds, connect timeout
    client.timeout = 600
    # Timeout advanced, connect / read timeout
    client.timeout = (3.05, 27)
```

### Limitations

There are currently no known limitations.

For more information please see: https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation

