#!/usr/bin/python

# Load the JSON module and use it to load your JSON file.                       
# I'm assuming that the JSON file contains a list of objects. 
# import Shutil brings in shell utilities which allows Python to interact in the command line, import os allows interaction with the operating system.                  
import json
import shutil
import os

print("{}").format(file)
## run your process on each file
for dirpath, subdirs, files in os.walk("./figures_json"):
    for the_file in files:
        if (the_file.split('.')[-1] != 'json'):
            continue
        the_fig_file = "./figures_json/"+the_file
        print("{}").format(the_fig_file)
        obj = json.load(open(the_fig_file))        
                                                            
        for i in xrange(len(obj)):
            obj[i][obj[i].keys()[0]].pop("outlines", None)
        updated_file = "./updated_files/"+the_file.split(".")[0]+"_updated.json"
                # Output the updated file with pretty JSON                                      
        open(updated_file, "wb").write(
            json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))