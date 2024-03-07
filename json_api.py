import json
from urllib.request import urlopen

with urlopen("https://masomomsingi.com/list-of-kcse-top-100-schools-nationally/") as response:
    source = response.read()

data = json.loads(source) #loading string
print(source)

