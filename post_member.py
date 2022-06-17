# !/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
"""Modules Needed"""
import json
import pprint
import requests

# Authentication Credentials
USERNAME = 'wrousseau95'
API_TOKEN = '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'

# Base Organization URL
URL = 'https://api.github.com/orgs/SledrosTestBox/invitations'

# New User's Info (roles available are, 'admin', 'direct_member', 'billing_manager)
NEW_UI = json.dumps({"email": 'wroussea1977@gmail.com',
                    "role": 'direct_member',
                    "team_ids": [6176431]})

# Invites a new user to an organization, and assigns a team with a confirmation prompt
while True:
    Confirmation = input('Are you sure you want to invite this user? Y/N\n')

# If Y/y is entered an invitation will be sent to the email
    if Confirmation in ('Y', 'y'):
        response = requests.post(URL, data=NEW_UI, auth=(USERNAME, API_TOKEN))
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
