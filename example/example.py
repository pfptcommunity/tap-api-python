import datetime
from datetime import timedelta, datetime, timezone

from tap_api.common.campaign.time_interval import StartOffsetInterval, StartEndInterval, OffsetEndInterval
from tap_api.v2 import Client

import json

if __name__ == '__main__':
    api_key_file = open("../tap.api_key", "r")
    api_key_data = json.load(api_key_file)
    api_key = api_key_data.get("demous")

    client = Client(api_key.get("PRINCIPAL"), api_key.get("SECRET"))
    print(client.siem.uri)
    print(client.forensics.uri)
    print(client.campaign.uri)
    print(client.campaign.ids.uri)

    campaign_data = client.campaign.ids(StartEndInterval(datetime.now(timezone.utc) - timedelta(hours=1), datetime.now(timezone.utc)))
    print(campaign_data.get_status())
    print(campaign_data.get_reason())
    for info in campaign_data.campaigns:
        print("\nCampaigns:")
        print(f"  ID: {info.id}")
        print(f"  Last Updated At: {info.last_updated_at}")
    exit(0)

    #aggregate_data = client.forensics.threat("982e999847425ff196939cb2385887f685b1fe0dcd258560cf4de3c7169cdcaa")
    aggregate_data = client.forensics.campaign("4a3df8c3-0055-4bc4-a150-73e81436871d")
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


    #
    # # Dump URI build
    # print(client.threat.uri)
    # print(client.threat.summary.uri)
    # print(client.threat.summary["f350d6ad78e52acde166d43e6b97baaf7944f966b4fd6cc4af96ae5b7a8c121c"].uri)
    #
    # Returns a threat summary dictionary
    # threat_summary = client.threat.summary["f350d6ad78e52acde166d43e6b97baaf7944f966b4fd6cc4af96ae5b7a8c121c"]()
    #
    # # Dictionary object also has data associated with the HTTP response.
    # print("HTTP Status:", threat_summary.get_status())
    # print("HTTP Reason:", threat_summary.get_reason())
    #
    # print("\nThreat Info:")
    # print(f"  ID: {threat_summary.id}")
    # print(f"  Identified At: {threat_summary.identified_at}")
    # print(f"  Name: {threat_summary.name}")
    # print(f"  Type: {threat_summary.type}")
    # print(f"  Category: {threat_summary.category}")
    # print(f"  Status: {threat_summary.status}")
    # print(f"  Detection Type: {threat_summary.detection_type}")
    # print(f"  Severity: {threat_summary.severity}")
    # print(f"  Attack Spread: {threat_summary.attack_spread}")
    # print(f"  Notable: {threat_summary.notable}")
    # print(f"  Verticals: {threat_summary.verticals}")
    # print(f"  Geographies: {threat_summary.geographies}")
    #
    # print("\n  Actors:")
    # for actor in threat_summary.actors:
    #     print(f"    ID: {actor.id}")
    #     print(f"    Name: {actor.name}")
    #
    # print("\n  Families:")
    # for family in threat_summary.families:
    #     print(f"    ID: {family.id}")
    #     print(f"    Name: {family.name}")
    #
    # print("\n  Malware:")
    # for malware in threat_summary.malware:
    #     print(f"    ID: {malware.id}")
    #     print(f"    Name: {malware.name}")
    #
    # print("\n  Techniques:")
    # for technique in threat_summary.techniques:
    #     print(f"    ID: {technique.id}")
    #     print(f"    Name: {technique.name}")
    #
    # print("\n  Brands:")
    # for brand in threat_summary.brands:
    #     print(f"    ID: {brand.id}")
    #     print(f"    Name: {brand.name}")

    #
    # # Test ThreatInfo object dump
    # print(json.dumps(threat_summary, indent=4))
    #
    # print(client.people.uri)
    # print(client.people.vap.uri)
    #
    # vap_info = client.people.vap()
    #
    # print("HTTP Status:", vap_info.get_status())
    # print("HTTP Reason:", vap_info.get_reason())
    # print("Total VAPs:", vap_info.total_vap_users)
    # print("Interval:", vap_info.interval)
    # print("Average Attack Index:", vap_info.average_attack_index)
    # print("VAP Attack Threshold:", vap_info.vap_attack_index_threshold)
    #
    # for user in vap_info.users:
    #     identity = user.identity
    #     threat_statistics = user.threat_statistics
    #
    #     print("\nUser Details:")
    #     print("  Email(s):", identity.emails)
    #     print("  Name:", identity.name or "N/A")
    #     print("  Department:", identity.department or "N/A")
    #     print("  Location:", identity.location or "N/A")
    #     print("  Title:", identity.title or "N/A")
    #     print("  VIP:", identity.vip)
    #
    #     print("Threat Statistics:")
    #     print("  Attack Index:", threat_statistics.attack_index)
    #     print("  Threat Families:")
    #     for family in threat_statistics.families:
    #         print(f"    - {family.name}: {family.score}")



    #print("VAP Info", json.dumps(vap_info, indent=4))

    # # Dump URI build
    # print(client.url.uri)
    #
    # decoded_urls = client.url.decode([
    #     "https://urldefense.proofpoint.com/v2/url?u=http-3A__links.mkt3337.com_ctt-3Fkn-3D3-26ms-3DMzQ3OTg3MDQS1-26r-3DMzkxNzk3NDkwMDA0S0-26b-3D0-26j-3DMTMwMjA1ODYzNQS2-26mt-3D1-26rt-3D0&d=DwMFaQ&c=Vxt5e0Osvvt2gflwSlsJ5DmPGcPvTRKLJyp031rXjhg&r=MujLDFBJstxoxZI_GKbsW7wxGM7nnIK__qZvVy6j9Wc&m=QJGhloAyfD0UZ6n8r6y9dF-khNKqvRAIWDRU_K65xPI&s=ew-rOtBFjiX1Hgv71XQJ5BEgl9TPaoWRm_Xp9Nuo8bk&e=",
    #     "https://urldefense.proofpoint.com/v1/url?u=http://www.bouncycastle.org/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a",
    #     "https://urldefense.com/v3/__https://google.com:443/search?q=a*test&gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$"
    # ])
    #
    # # DictionaryCollection object also has data associated with the HTTP response.
    # print("HTTP Status:", decoded_urls.get_status())
    # print("HTTP Reason:", decoded_urls.get_reason())
    # print("Response Data:", json.dumps(decoded_urls, indent=4))
    # for url_info in decoded_urls.urls():
    #     print("\nDecoded URL Info:")
    #     print(f"  Encoded URL: {url_info.encoded_url}")
    #     print(f"  Decoded URL: {url_info.decoded_url}")
    #     print(f"  Message GUID: {url_info.message_guid}")
    #     print(f"  Cluster Name: {url_info.cluster_name}")
    #     print(f"  Recipient Email: {url_info.recipient_email}")
    #     print(f"  Success: {url_info.success}")
    #     print(f"  Error: {url_info.error or 'N/A'}")