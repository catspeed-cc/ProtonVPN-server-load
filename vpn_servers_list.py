import vpn_servers as vpns

#
# We test by searching for location = "US-" servers under 40% load to get all United States servers
# You could also search for location = "US-CO" for example, to get all Colorado, United States servers
#
# If searching only by 2 letter country code, you must include the - at the end.
# This is to prevent finding states when you want countries.
#
vpns.find_a_server(location = "CA-", num_results = 5, max_load = 40)
