import json
import requests

response = requests.get('https://api.protonmail.ch/vpn/logicals')
servers_dict = json.loads(response.text)

# Get rid of the LogicalServers wrapper
servers_list = servers_dict['LogicalServers']

# Compile all server names into single list
server_names = []
for x in range(len(servers_list)):
    server_names.append(servers_list[x]['Name'])

# Compile all server hostnames into single list
server_hostnames = []
for x in range(len(servers_list)):
    server_hostnames.append(servers_list[x]['Domain'])

# Compile all server load values into single list
server_load = []
for x in range(len(servers_list)):
    server_load.append(servers_list[x]['Load'])

# Compile all server tier values into single list
server_tier = []
for x in range(len(servers_list)):
    server_tier.append(servers_list[x]['Tier'])

    
def find_a_server_in(location = 'US', num_results = 5, max_load = 30):
    draw = 0
    # Look for servers in given location
    index = []
    for i,x in enumerate(server_names):
        if location in x:
            index.append(i)

    # Look for tier 1 and 2 servers in given location
    temp = []
    for i in index:
        if server_tier[i] == 1:
            temp.append(i)
        if server_tier[i] == 2:
            temp.append(i)

    index = temp

    # Compile list of server load values
    # for tier 1 and 2 servers in given location
    load_list = []
    for i in index:
        load_list.append(server_load[i])
    
    filtered_list = []
    for i,x in index:
        if load_list[x] <= max_load:
            filtered_list.append(i)

    # load list is list of ALL server load values (parallel array)
    #print(load_list)

    #print(index)
    #print(temp)
    #print(server_names)
    #print(server_load)
    #print(server_tier)

    #print(index)
    print(filtered_list)
    #print(index[index_lowest])

    # Get index of lowest load
    filtered_list = [i for i, j in enumerate(load_list) if j == min(load_list)]

    if len(filtered_list) == 1:
        index_lowest = filtered_list[0]
    elif len(filtered_list) > 1:
        draw = 1
        index_lowest_2 = filtered_list[1]
        index_lowest = filtered_list[0]
    else:
        print("error getting len(filtered_list)")
        print(filtered_list)

    #print(min(load_list))
    #print(index_lowest)
    #print(filtered_list)

    # Get the name of the server with lowest load
    the_server = server_names[index[index_lowest]]
    the_hostname = server_hostnames[index[index_lowest]]
    the_load = load_list[index_lowest]
    the_tier = server_tier[index_lowest]

    print("Server: " + the_server + " Hostname: " + the_hostname + " Load: " + str(the_load) + "% Tier: " + str(the_tier))
    
    # If there's a draw, print out the other contending server
    if draw == 1:
        the_server_2 = server_names[index[index_lowest_2]]
        the_hostname_2 = server_hostnames[index[index_lowest_2]]
        the_load_2 = load_list[index_lowest_2]
        the_tier_2 = server_tier[index_lowest_2]
        
        print("Server: " + the_server_2 + " Hostname: " + the_hostname_2 + " Load: " + str(the_load_2) + "% Tier: " + str(the_tier_2))


# testing the function
find_a_server_in(location = "US", num_results = 5, max_load = 30)
