# ProtonVPN-server-load

Script to print out all servers under the desired maximum load, sorted by load from highest to lowest.

Uses the ProtonVPN API [https://vpn-api.proton.me/vpn/logicals](https://vpn-api.proton.me/vpn/logicals) and pycountry python library [https://pypi.org/project/pycountry/](https://pypi.org/project/pycountry/)

Script was cloned from [https://github.com/akazukin5151/ProtonVPN-server-load](https://github.com/akazukin5151/ProtonVPN-server-load), fixed, and heavily modified to suit my needs.

I am going to try either outputting ovpn config files, or a servers.json for use with gluetun. Probably the latter, because generating configs would be lots more work. I only need this to generate config for gluetun so a servers.json for gluetun might be all that I do. If you wish to see it generate also wg/openvpn config files, please let me know by creating an issue ticket https://gitea.catspeed.cc/catspeed-cc/ProtonVPN-server-load/issues

**Note:** Currently script is only able to get Tier 2 (premium) servers. I am trying to find the API for Tiers 0 & 1.<br />
**Note:** Currently num_results is not implemented. It will take minimal work to get it working.

- If you get too many results, lower max_load.
- If you get too few or zero results, increase max_load
- If still have issues, ensure that you are using the correct two letter country_code (or state_code)

This documentation will be updated when work is complete.

## Installation:

- ```apt install python3 python3-full python3-requests python3-pycountry```
- ```git clone https://gitea.catspeed.cc/catspeed-cc/ProtonVPN-server-load```
- ```cd ProtonVPN-server-load```

## Usage:

**in bash**: you will need to modify vpn_servers_list.py to get desired servers, then run the command:
```sh
python vpn_servers_list.py
>>> Server[33]: US-NJ#9 Hostname: node-us-31.protonvpn.net City: Secaucus Load: 40% Tier: 2 secure_core: True netshield: True port_forward: True
>>> Server[34]: US-NJ#10 Hostname: node-us-31.protonvpn.net City: Secaucus Load: 40% Tier: 2 secure_core: True netshield: True port_forward: True
>>> Server[664]: US-CA#197 Hostname: node-us-168.protonvpn.net City: Los Angeles Load: 40% Tier: 2 streaming: True port_forward: True
>>> Server[1263]: US-CA#321 Hostname: node-us-212.protonvpn.net City: Los Angeles Load: 40% Tier: 2 streaming: True port_forward: True

```

OR

**in python**:
```py
import vpn_servers as vpns

print("US-CA# servers:")
vpns.find_a_server(country_code = "US", state_code = "CA", max_load = 40, num_results = 5)
>>> US-CA# servers:
>>> Server[1276]: US-CA#310 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 34% Tier: 2 streaming: True port_forward: True
>>> Server[1275]: US-CA#309 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True
>>> Server[1278]: US-CA#312 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True
>>> Server[1279]: US-CA#313 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True

print("US-xx# servers:")
vpns.find_a_server(country_code = "US", state_code = "", max_load = 40, num_results = 5)
>>> US-xx# servers:
>>> Server[1369]: US-UT#51 Hostname: node-us-226.protonvpn.net City: Salt Lake City Load: 33% Tier: 2 secure_core: True netshield: True port_forward: True
>>> Server[525]: US-UT#37 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 15% Tier: 2 streaming: True
>>> Server[526]: US-UT#39 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 13% Tier: 2 streaming: True
>>> Server[527]: US-UT#40 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 11% Tier: 2 streaming: True

print("CA# servers:")
vpns.find_a_server(country_code = "CA", state_code = "", max_load = 40, num_results = 5)
>>> CA# servers:
>>> Server[3119]: CA#488 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3121]: CA#490 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3122]: CA#491 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3127]: CA#496 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True

```

You can get the country codes from:
- https://en.wikipedia.org/wiki/ISO_3166-1

You can get state/province codes from:
- https://en.wikipedia.org/wiki/ISO_3166-2:US
- https://en.wikipedia.org/wiki/ISO_3166-2:CA
- you can change the country code on the end of the URL to get others
