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

# Compile all server hostnames into single list
server_cities = []
for x in range(len(servers_list)):
    server_cities.append(servers_list[x]['City'])

# Compile all server load values into single list
server_load = []
for x in range(len(servers_list)):
    server_load.append(servers_list[x]['Load'])

# Compile all server tier values into single list
server_tier = []
for x in range(len(servers_list)):
    server_tier.append(servers_list[x]['Tier'])

# Compile all server features values into single list
server_features = []
for x in range(len(servers_list)):
    server_features.append(servers_list[x]['Features'])

def convert_features(features = 1):
    error = False

    if (features >= 20):
        features = features - 20
        port_forward = True
    else:
        port_forward = False

    if (features >= 8):
        features = features - 8
        streaming = True
    else:
        streaming = False

    if (features >= 3):
        features = features - 3
        netshield = True
    else:
        netshield = False

    if (features >= 1):
        features = features - 1
        secure_core = True
    else:
        secure_core = False

    # sanity check, features should now equal 0
    if (features == 0):
        error = False
    else:
        error = True
    
    return error, secure_core, netshield, streaming, port_forward

def find_a_server(location = 'US', num_results = 5, max_load = 30):
    draw = 0
    # Look for servers in given location
    index = []
    for i,x in enumerate(server_names):
        if location in x:
            index.append(i)

    # Look for tier 1 and 2 servers in given location
    temp = []
    for i in index:
        if server_tier[i] == 0:
            temp.append(i)
        if server_tier[i] == 1:
            temp.append(i)
        if server_tier[i] == 2:
            temp.append(i)

    index = temp

    # index is list of all tier 1 & 2 servers
    #print(index)

    # Compile list of server load values
    # for tier 1 and 2 servers in given location
    load_list = []
    for i in index:
        load_list.append(server_load[i])

    # load list is list of all tier 1 & 2 servers load values
    #print(load_list)
    
    filtered_list = []
    for i in index:
        if server_load[i] <= max_load:
            filtered_list.append(i)

    for i in filtered_list:
        # display each server in the list
        the_server = server_names[i]
        the_hostname = server_hostnames[i]
        the_city = server_cities[i]
        the_load = server_load[i]
        the_tier = server_tier[i]
        error, secure_core, netshield, streaming, port_forward = convert_features(server_features[i])
        
        addstr = ""
        if secure_core:
            addstr += " secure_core: True"
        if netshield:
            addstr += " netshield: True"
        if streaming:
            addstr += " streaming: True"
        if port_forward:
            addstr += " port_forward: True"
        if error:
            addstr += " error parsing features, features = " + str(server_features[i])

        print("Server[" + str(i) + "]: " + the_server + " Hostname: " + the_hostname + " City: " + the_city + " Load: " + str(the_load) + "% Tier: " + str(the_tier) + addstr)

