import vpn_servers as vpns

#
# You can pass in either only 2 letter country code, or 2 letter country code and 2 letter state code.
#
# Note most countries do not have state_codes - or province codes - listed, ex. Canada, Chile, Germany, etc.
#
# Easiest method is to try searching country code only, and then look at the results, and then search 
# country_code & state_code if you see servers with state codes (Ex. US-CA#151)
#
print("US-CA# servers:")
vpns.find_a_server(country_code = "US", state_code = "CA", max_load = 60, num_results = 5)
print("US-xx# servers:")
vpns.find_a_server(country_code = "US", state_code = "", max_load = 40, num_results = 5)
print("CA# servers:")
vpns.find_a_server(country_code = "CA", state_code = "", max_load = 60, num_results = 5)
