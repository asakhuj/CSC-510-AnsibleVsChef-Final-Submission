import requests
import json
r = requests.get('https://api.github.com/repos/chef/chef')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print("***************************************************")
    print ("Chef repository created: " + repoItem['created_at'])
    print ("Open issues in chef : "+ str(repoItem['open_issues']))
