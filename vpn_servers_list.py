import vpn_servers as vpns

#
# You can pass in either only 2 letter country code, or 2 letter country code and 2 letter state code.
#
# Note most countries do not have state_codes - or province codes - listed, ex. Canada, Chile, Germany, etc.
#
# It is best to search with a state/province code, because if no results are found, it will fall back to search country only
#
# If no results are found, try increasing max_load and check the API works https://vpn-api.proton.me/vpn/logicals
#
print("US-CA# servers:")
vpns.find_a_server(country_code = "US", state_code = "CA", max_load = 40, num_results = 5)
print("US-xx# servers:")
vpns.find_a_server(country_code = "US", state_code = "", max_load = 40, num_results = 5)
print("CA# servers:")
vpns.find_a_server(country_code = "CA", state_code = "", max_load = 40, num_results = 5)
