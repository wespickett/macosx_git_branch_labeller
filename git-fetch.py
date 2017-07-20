import sys
import requests #pip install requests
import os

BRANCH = sys.argv[1]

authFile = open(os.path.dirname(__file__) + '/.fetch-auth', 'r')
authLines = authFile.read().splitlines()
authFile.close()

response = requests.get('https://insidevault.atlassian.net/rest/api/2/search?jql=key=' + BRANCH + '&fields=summary',
                         auth=(authLines[0], authLines[1]))

data = response.json()

if len(data) and "issues" in data and len(data["issues"]) and "fields" in data["issues"][0] and "summary" in data["issues"][0]["fields"]:
	print data["issues"][0]["fields"]["summary"]
