import requests
import json
r = requests.get('https://api.github.com/repos/ansible/ansible')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print ("Ansible repository created: " + repoItem['created_at'])
