import vpn_servers as vpns

# We test by searching for location = "US" servers under 40% load to get all United States servers
# You could also search for location = "US-CO" for example, to get all Colorado, United States servers
vpns.find_a_server(location = "US", num_results = 5, max_load = 95)
