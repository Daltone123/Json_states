'''Javascript Object Notation'''

import json
#loading the json file
with open('states.json') as f:
    #loading the file states.json into a python object
    data = json.load(f)

#looping through the data with the key 'states'
for states in data['states']:
    print(states['name'], states['abbreviation'])

    #to remove area code
    #del (states['area_codes'])

# #writing back as json
#with open('new_states.json', 'w') as f:
    #json.dumb(data, f)





