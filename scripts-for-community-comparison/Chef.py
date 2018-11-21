import requests
import json
r = requests.get('https://api.github.com/repos/chef/chef')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print ("Chef repository created: " + repoItem['created_at'])
