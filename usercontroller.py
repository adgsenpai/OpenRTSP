# usercontroller.py
# used to auth users for web portal

import yaml

database = {}
with open(r'./appconfig.yaml') as ymlfile:
     documents = yaml.full_load(ymlfile)
     for item in documents:
        database.update(item)

usernames = list(database['accounts'][0]['usernames'])
passwords = list(database['accounts'][1]['passwords'])

userauth =  {usernames[i]: passwords[i] for i in range(len(usernames))}
print(userauth)

def AuthUser(username,password):
        if str(password) == str(userauth[str(username)]):
            return True
        else:
            return False
def ReturnCameras():
    return list(database['ipcameras'])

