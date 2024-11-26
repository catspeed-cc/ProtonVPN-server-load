# ProtonVPN-server-load

Script to print out all servers under the desired maximum load

Script was cloned from [https://github.com/akazukin5151/ProtonVPN-server-load](https://github.com/akazukin5151/ProtonVPN-server-load), fixed, and heavily modified to suit my needs.

Uses the ProtonVPN API [https://api.protonmail.ch/vpn/logicals](https://api.protonmail.ch/vpn/logicals)

Currently the script is only able to get Tier 2 servers because those are the only servers the API is listing. I am trying to figure out how to get Tier 0 (free) and Tier 1 (basic) servers.

It will sort the list from highest to lowest, so the lowest load shows at the bottom.

**Note:** Currently num_results is not implemented. It will take minimal work to get it working.<br />
**Note:** I am going to try either outputting ovpn configuration files, or a servers.json for use with gluetun

This documentation will be updated when work is complete.

## Usage:

**in bash**:
```
python vpn_servers_list.py
```

OR

**in python**:
```py
import vpn_servers as vpns

print("US-CA# servers:")
vpns.find_a_server(country_code = "US", state_code = "CA", max_load = 40, num_results = 5)
>>> Server[1276]: US-CA#310 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 34% Tier: 2 streaming: True port_forward: True
>>> Server[1275]: US-CA#309 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True
>>> Server[1278]: US-CA#312 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True
>>> Server[1279]: US-CA#313 Hostname: node-us-211.protonvpn.net City: Los Angeles Load: 33% Tier: 2 streaming: True port_forward: True

print("US-xx# servers:")
vpns.find_a_server(country_code = "US", state_code = "", max_load = 40, num_results = 5)
>>> Server[1369]: US-UT#51 Hostname: node-us-226.protonvpn.net City: Salt Lake City Load: 33% Tier: 2 secure_core: True netshield: True port_forward: True
>>> Server[525]: US-UT#37 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 15% Tier: 2 streaming: True
>>> Server[526]: US-UT#39 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 13% Tier: 2 streaming: True
>>> Server[527]: US-UT#40 Hostname: node-us-158.protonvpn.net City: Salt Lake City Load: 11% Tier: 2 streaming: True

print("CA# servers:")
vpns.find_a_server(country_code = "CA", state_code = "", max_load = 40, num_results = 5)
>>> Server[3119]: CA#488 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3121]: CA#490 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3122]: CA#491 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True
>>> Server[3127]: CA#496 Hostname: node-ca-33.protonvpn.net City: Vancouver Load: 40% Tier: 2 secure_core: True netshield: True streaming: True

```

You can get the country codes [here](https://protonvpn.com/vpn-servers)
