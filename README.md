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

### Creating an API client object

```python
from tap_api.v2 import *

if __name__ == '__main__':
    client = Client("<principal>", "<secret>")
```

### Querying the Forensics API

```python
if __name__ == '__main__':
    client = Client("<principal>", "<secret>")
    print(client.siem.uri)
    print(client.forensics.uri)
    aggregate_data = client.forensics.threat("<threat_id_here>")
    print("HTTP Status:", aggregate_data.get_status())
    print("HTTP Reason:", aggregate_data.get_reason())
    for report in aggregate_data.reports:
        print("\nReport:")
        print(f"  Scope: {report.scope}")
        print(f"  ID: {report.id}")
        print(f"  Name: {report.name}")
        print(f"  Threat Status: {report.threat_status}")

        for forensic in report.forensics:
            print("\n  Forensic:")
            print(f"    Type: {forensic.type}")
            print(f"    Display: {forensic.display}")
            print(f"    Engine: {forensic.engine}")
            print(f"    Malicious: {forensic.malicious}")
            print(f"    Time: {forensic.time}")
            print(f"    Note: {forensic.note or 'N/A'}")

            # Dump the `what` object. Note helper properties exist, but you must know the object type or type. 
            print("    What {}:".format(type(forensic.what).__name__))
            print(json.dumps(forensic.what, indent=4))

            # Dump platforms if available
            if forensic.platforms:
                print("    Platforms:")
                for platform in forensic.platforms:
                    print(f"      Name: {platform.name}")
                    print(f"      OS: {platform.os}")
                    print(f"      Version: {platform.version}")
```

### Querying the Threats API

```python
if __name__ == '__main__':
    client = Client("<principal>", "<secret>")

    # Returns a threat summary dictionary
    threat_summary = client.threat.summary["<threat_id>"]()

    # Dictionary object also has data associated with the HTTP response.
    print("HTTP Status:", threat_summary.get_status())
    print("HTTP Reason:", threat_summary.get_reason())

    print("\nThreat Info:")
    print(f"  ID: {threat_summary.id}")
    print(f"  Identified At: {threat_summary.identified_at}")
    print(f"  Name: {threat_summary.name}")
    print(f"  Type: {threat_summary.type}")
    print(f"  Category: {threat_summary.category}")
    print(f"  Status: {threat_summary.status}")
    print(f"  Detection Type: {threat_summary.detection_type}")
    print(f"  Severity: {threat_summary.severity}")
    print(f"  Attack Spread: {threat_summary.attack_spread}")
    print(f"  Notable: {threat_summary.notable}")
    print(f"  Verticals: {threat_summary.verticals}")
    print(f"  Geographies: {threat_summary.geographies}")

    print("\n  Actors:")
    for actor in threat_summary.actors:
        print(f"    ID: {actor.id}")
        print(f"    Name: {actor.name}")

    print("\n  Families:")
    for family in threat_summary.families:
        print(f"    ID: {family.id}")
        print(f"    Name: {family.name}")

    print("\n  Malware:")
    for malware in threat_summary.malware:
        print(f"    ID: {malware.id}")
        print(f"    Name: {malware.name}")

    print("\n  Techniques:")
    for technique in threat_summary.techniques:
        print(f"    ID: {technique.id}")
        print(f"    Name: {technique.name}")

    print("\n  Brands:")
    for brand in threat_summary.brands:
        print(f"    ID: {brand.id}")
        print(f"    Name: {brand.name}")
```

### Querying the People API

```python
if __name__ == '__main__':
    client = Client("<principal>", "<secret>")
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
    client = Client("<principal>", "<secret>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('socks5', credentials, '<your_proxy>', '8128')}
```

HTTP Proxy Example (Squid):

```python
from tap_api.v3 import *

if __name__ == '__main__':
    client = Client("<principal>", "<secret>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('http', credentials, '<your_proxy>', '3128')}

```

### HTTP Timeout Settings

```python
from tap_api.v3 import *

if __name__ == '__main__':
    client = Client("<principal>", "<secret>")
    # Timeout in seconds, connect timeout
    client.timeout = 600
    # Timeout advanced, connect / read timeout
    client.timeout = (3.05, 27)
```

### Limitations

There are currently no known limitations.

For more information please see: https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation

