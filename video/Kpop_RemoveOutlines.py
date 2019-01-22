# Load the JSON module and use it to load your JSON file.                       
# I'm assuming that the JSON file contains a list of objects.                   
import json
obj  = json.load(open("zYoYoBtLqOY_figures.json"))

# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.         
                                           
for i in xrange(len(obj)):
    obj[i][obj[i].keys()[0]].pop("outlines", None)

# Output the updated file with pretty JSON                                      
open("updated-zYoYoBtLqOY_figures.json", "w").write(
    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
)
