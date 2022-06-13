#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# Modules Needed
# import pprint
import requests


# Credentials
USERNAME = 'wrousseau95'
API_TOKEN = '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'

# Base Organization URL
URL = 'https://api.github.com/orgs/SledrosTestBox'

# Endpoint for Members List
MEMBER = '/members'

# Endpoint for Teams List
TEAM = '/teams'

# Endpoint for if you wish to call a specific user
USER = '/memberships/WoodyR13'

# GET Request of the Organizations Members/Teams Data / Specific User
r_mem = requests.get(URL+MEMBER, auth=(USERNAME, API_TOKEN))
r_team = requests.get(URL+TEAM, auth=(USERNAME, API_TOKEN))
r_user = requests.get(URL+USER, auth=(USERNAME, API_TOKEN))

# To Display All Data in JSON Format for Members/Teams / Specific User
# pprint.pprint(r_mem.json())
# pprint.pprint(r_team.json())
# pprint.pprint(r_user.json())

# To Query Specific Fields for Members(Enter amount of members within range)
print("\nMEMBER LIST:")
for x in range(2):
    print("Username: " + r_mem.json()[x]['login'])
    print("ID #: " + str(r_mem.json()[x]['id']))
    print(("User URL: " + r_mem.json()[x]['html_url']), '\n')

# To Query Specific Fields for Teams(Enter amount of teams within range)
print("\nTEAM LIST:")
for y in range(1):
    print("Team Name: " + r_team.json()[y]['name'])
    print("Team ID #: " + str(r_team.json()[y]['id']))
    print("Team URL: " + r_team.json()[y]['html_url'], '\n')

# To Query Specific Fields About A Specific User
print("\nUSER DATA:")
print("Username: "+r_user.json()['user']['login'])
print("User ID #: "+str(r_user.json()['user']['id']))
print("User Role: "+r_user.json()['role'])
print("Organization: "+r_user.json()['organization']['login'])
print("Organization ID #: "+str(r_user.json()['organization']['id']))

