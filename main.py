import sys
import json
from with_argv import With_argv

fileBuffer = None
size = int(0)

with open('data.json') as file:
    fileBuffer = json.load(file)
    size = fileBuffer['size']

if len(sys.argv) > 1:
    With_argv.Parse_argv(sys.argv)
    

    












