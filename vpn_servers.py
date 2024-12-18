import json
import requests
import pycountry

response = requests.get('https://vpn-api.proton.me/vpn/logicals')
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

# Compile all servers into single list
server_servers = []
for x in range(len(servers_list)):
    server_servers.append(servers_list[x]['Servers'])

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

def find_a_server(country_code = "US", state_code = "", num_results = 5, max_load = 30):

    # decide what string to search for
    if state_code == "":
        search_for = country_code + "-"
        search_for_alt = country_code + "#"
        country_only = True
    else:
        search_for = country_code + "-" + state_code + "#"
        country_only = False

    draw = 0
    # Look for servers in given location
    index = []
    for i,x in enumerate(server_names):
        if search_for in x:
            index.append(i)

    if country_only and len(index) == 0:
        # Look for servers in given location
        index = []
        for i,x in enumerate(server_names):
            if x.startswith(search_for_alt):
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
    
    # filter the list to only have servers with loads under max_load
    filtered_list = []
    for i in index:
        if server_load[i] <= max_load:
            filtered_list.append(i)

    # reorder by server load
    filtered_list_max_index = len(filtered_list)
    # loop from max_load to 1 stepping by -1
    temp = []
    for x in range(max_load, 1, -1):
        # loop over list checking load
        for y in filtered_list:
            if server_load[y] == x:
                temp.append(y)

    filtered_list = temp

    # loop through the filtered list and extract values
    for i in filtered_list:
        # display each server in the list
        the_server = server_names[i]
        the_hostname = server_hostnames[i]
        the_load = server_load[i]
        the_tier = server_tier[i]

        error, secure_core, netshield, streaming, port_forward = convert_features(server_features[i])

        entry_ip = server_servers[i][0]['EntryIP']
        exit_ip = server_servers[i][0]['ExitIP']
        pub_key = server_servers[i][0]['X25519PublicKey']

        the_lat = servers_list[i]['Location']['Lat']
        the_long = servers_list[i]['Location']['Long']

        # get the country
        the_country = pycountry.countries.get(alpha_2=the_server[0:2]).name

        # get the state
        if the_server.find("-") > 0:
            #the_state = the_server[the_server.find("-")+len("-"):the_server.rfind("#")]
            the_state = pycountry.subdivisions.get(code=the_server[0:5]).name
        else:
            the_state = "null"
        
        # moved here to keep it with country/state
        the_city = server_cities[i]

        if len(server_servers[i]) > 1:
            print("WARN: len(server_servers[]) = " + str(len(server_servers[i])) + "! Expected 1!")
        
        addstr = ""
        if secure_core:
            addstr += " secure_core[True]"
        if netshield:
            addstr += " netshield[True]"
        if streaming:
            addstr += " streaming[True]"
        if port_forward:
            addstr += " port_forward[True]"
        if error:
            addstr += " error parsing features, features = " + str(server_features[i])

        print("Server[" + str(i) + "]: [" + the_server + "] Hostname[" + the_hostname + "] Country[" + str(the_country) + "] State[" + str(the_state) + "] City[" + str(the_city) + "] Load[" + str(the_load) + "%] Tier[" + str(the_tier) + "] Entry[" + entry_ip + "] Exit[" + exit_ip + "] Lat[" + str(the_lat) + "] Long[" + str(the_long) + "] PubKey[" + pub_key + "]" + addstr)

