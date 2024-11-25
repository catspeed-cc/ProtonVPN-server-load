# ProtonVPN-server-load

Script to print out all servers under the desired maximum load

Script was cloned from [https://github.com/akazukin5151/ProtonVPN-server-load](https://github.com/akazukin5151/ProtonVPN-server-load), fixed, and heavily modified to suit my needs.

Uses the ProtonVPN API [https://api.protonmail.ch/vpn/logicals](https://api.protonmail.ch/vpn/logicals)

Servers are restricted based on your plan (free, basic, plus), which corresponds to the Tier value of each server. Tier 0 is free, Tier 1 is basic, Tier 2 is plus.

This documentation will be updated when work is complete.

## Usage:

```py
>>> import vpn_servers as vpns
>>> vpns.find_a_server_in("JP")
JP#25: 6%
>>> vpns.find_a_server_in("CH") # Switzerland
CH#5: 15%
```

You can get the country codes [here](https://protonvpn.com/vpn-servers)
