#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# Modules Needed
import json
import pprint
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

# Endpoint for if you wish to call a specific user/remove user from organization
USER = '/memberships/WoodyR13'

# Teams Endpoint if you wish to just remove the user from a team
TEAMDEL = '/teams/TeamDro/memberships/WoodyR13'

# Endpoint for invitations to a team or an organization
INVITE = '/invitations'

# New User's Info (roles available are, 'admin', 'direct_member', 'billing_manager)
NEW_UI = json.dumps({"email": 'wroussea1977@gmail.com',
                    "role": 'direct_member',
                    "team_ids": [6176431]})

# Prompt to find out what kind of API request should be called per your need
while True:
    choice = input('Would you like to "view" organizational data, "invite" a new member, or "delete" a new member?\n'
                   'Please enter view, invite, or delete: ')

    if choice in ("View", "view"):
        # GET Request of the Organizations Members/Teams Data / Specific User
        r_mem = requests.get(URL + MEMBER, auth=(USERNAME, API_TOKEN))
        r_team = requests.get(URL + TEAM, auth=(USERNAME, API_TOKEN))
        r_user = requests.get(URL + USER, auth=(USERNAME, API_TOKEN))

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
        print("Username: " + r_user.json()['user']['login'])
        print("User ID #: " + str(r_user.json()['user']['id']))
        print("User Role: " + r_user.json()['role'])
        print("Organization: " + r_user.json()['organization']['login'])
        print("Organization ID #: " + str(r_user.json()['organization']['id']))
        break

    if choice in ("Invite", "invite"):
        # Invites a new user to an organization, and assigns a team with a confirmation prompt
        while True:
            Confirmation = input('Are you sure you want to invite this user? Y/N\n')

            # If Y/y is entered an invitation will be sent to the email
            if Confirmation in ('Y', 'y'):
                response = requests.post(URL + INVITE, data=NEW_UI, auth=(USERNAME, API_TOKEN))
                pprint.pprint(response.json())
                print(response)
                break
            # If N/n is entered the invitation will be aborted
            if Confirmation in ('N', 'n'):
                print("Invite aborted")
                break
            # If anything else is entered you will be asked to re-enter a proper option
            if Confirmation not in ('Y', 'y', 'N', 'n'):
                print("Invalid Option, Try Again.\n")
                
        # Exit code [0] or a Response [201] means the invitation was sent successfully
        break

    if choice in ("Delete", "delete"):
        # Removes a User from an Organization/Team with a confirmation prompt
        while True:
            Confirmation = input('Are you sure you want to remove this user from the Organization? Y/N\n')

            # If Y/y is entered the deletion of the user will proceed
            if Confirmation in ('Y', 'y'):
                response = requests.delete(URL + '<ENDPOINT>' + USER, auth=(USERNAME, API_TOKEN))
                print(response)
                break
            # If N/n is entered the deletion will be aborted
            if Confirmation in ('N', 'n'):
                print("Removal aborted")
                break
            # If anything else is entered you will be asked to re-enter a proper option
            if Confirmation not in ('Y', 'y', 'N', 'n'):
                print("Invalid Option, Try Again.\n")

        # [204] Status Code is a Successful Deletion
        # If user is not in the organization but has been sent an invitation, that will be revoked
        break
        
