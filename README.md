# wineapp
wine repo


Main:
Currently, main comes up with imaginary wines and plots them against each other
- the old code is already preserved
- It will be used as sergeant and main interface

Athena.py pings Athena on AWS with a specific SQL search
- The output is sent to the file "raw data"

jsonparsing.py reads a dictionary akin to the Athena output and outputs a cleaned up json file called dump.json
- it should be renamed
- it should follow Athena
