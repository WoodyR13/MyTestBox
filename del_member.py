# !/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
"""Modules Needed"""
import requests

# Authentication Credentials
USERNAME = 'wrousseau95
API_TOKEN = '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'

# Base Organization URL
URL = 'https://api.github.com/orgs/SledrosTestBox'

# Teams Endpoint if you wish to just remove the user from a team
TEAM = '/teams/TeamDro/memberships'

# Members Endpoint if you with to remove the user from the organization entirely
MEMBER = '/memberships'

# User to be Deleted
USER = '/WoodyR13'

# Removes a User from an Organization/Team with a confirmation prompt
while True:
    Confirmation = input('Are you sure you want to remove this user from the Organization? Y/N\n')

# If Y/y is entered the deletion of the user will proceed
    if Confirmation in ('Y', 'y'):
        response = requests.delete(URL+MEMBER+USER, auth=(USERNAME, API_TOKEN))
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
