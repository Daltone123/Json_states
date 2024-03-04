'''Javascript Object Notation'''

import json
#loading the json file
with open('states.json') as f:
    #loading the file states.json into a python object
    data = json.load(f)

#looping through the data with the key 'states'
for states in data:
    print(states)