import json
filename = 'Model/Config.json'
with open(filename) as iterator:
   jsonObject = json.loads(iterator.read())
   for key in jsonObject:
      value = jsonObject[key]
      print("The key and value are ({}) = ({})".format(key, value))
      print(value)
   
   
