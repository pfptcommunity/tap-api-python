import json
from typing import Dict

from tap_api.common.people.filters import TimeWindow
from tap_api.v2 import Client

if __name__ == '__main__':
    api_key_file = open("../tap.api_key", "r")
    api_key_data = json.load(api_key_file)
    api_key = api_key_file.read()

    client = Client(api_key_data.get("PRINCIPAL"), api_key_data.get("SECRET"))
    print(client.siem.uri)
    print(client.forensics.uri)
    # threat_data = client.forensics.threat("982e999847425ff196939cb2385887f685b1fe0dcd258560cf4de3c7169cdcaa")
    # for d in threat_data.reports:
    #     for f in d.forensics:
    #         print(json.dumps(f.what, indent=4))

    print(client.campaign.uri)
    #
    # # Dump URI build
    # print(client.threat.uri)
    # print(client.threat.summary.uri)
    # print(client.threat.summary["982e999847425ff196939cb2385887f685b1fe0dcd258560cf4de3c7169cdcaa"].uri)
    #
    # # Returns a threat summary dictionary
    # threat_summary = client.threat.summary["982e999847425ff196939cb2385887f685b1fe0dcd258560cf4de3c7169cdcaa"]()
    #
    # # Dictionary object also has data associated with the HTTP response.
    # print("HTTP Status:", threat_summary.get_status())
    # print("HTTP Reason:", threat_summary.get_reason())
    #
    # # Helpers are provided to quicly access the data with auto-completion.
    # print("Threat ID:", threat_summary.id)
    # print("Identified At:", threat_summary.identified_at)
    # print("Threat Name:", threat_summary.name)
    # print("Threat Type:", threat_summary.type)
    # print("Threat Category:", threat_summary.category)
    # print("Threat Status:", threat_summary.status)
    # print("Detection Type:", threat_summary.detection_type)
    # print("Severity Level:", threat_summary.severity)
    # print("Notable:", threat_summary.notable)
    # print("Verticals Affected:", threat_summary.verticals)
    # print("Geographies Impacted:", threat_summary.geographies)
    # print("Actors Involved:", threat_summary.actors)
    # print("Families Associated:", threat_summary.families)
    # print("Malware Identified:", threat_summary.malware)
    # print("Techniques Used:", threat_summary.techniques)
    # print("Brands Affected:", threat_summary.brands)
    #
    # # Test ThreatInfo object dump
    # print(json.dumps(threat_summary, indent=4))
    #
    # print(client.people.uri)
    # print(client.people.vap.uri)
    #
    vap_info = client.people.vap()

    print("HTTP Status:", vap_info.get_status())
    print("HTTP Reason:", vap_info.get_reason())
    print("Users:", vap_info.users)
    print("Total Vaps:", vap_info.total_vap_users)
    print("Interval:", vap_info.interval)
    print("Cluster Name:", vap_info.average_attack_index)
    print("Recipient Email:", vap_info.average_attack_index)
    print("VAP Info", json.dumps(vap_info, indent=4))

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
    #     print("Encoded URL:", url_info.encoded_url)
    #     print("Decoded URL:", url_info.decoded_url)
    #     print("Message GUID:", url_info.message_guid)
    #     print("Cluster Name:", url_info.cluster_name)
    #     print("Recipient Email:", url_info.recipient_email)
    #     print("Success:", url_info.success)
    #     print("Error:", url_info.error)
    #     print("URL Info", json.dumps(url_info, indent=4))