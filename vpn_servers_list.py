import vpn_servers as vpns

#
# We test by searching for location = "US-" servers under 40% load to get all United States servers
# You could also search for location = "US-CO" for example, to get all Colorado, United States servers
#
# If searching only by 2 letter country code, you must include the - at the end.
# This is to prevent finding states when you want countries.
#
# In the case of searching for Canada servers, there appears to be no state/province code
# Thus you should search for CA# instead
#
# You can search for the 2 letter country code with a - at the end, and if you get nothing, try it with a # at the end.
#
vpns.find_a_server(location = "CA#", num_results = 5, max_load = 40)
