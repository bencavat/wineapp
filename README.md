# wineapp
wine repo

Fix typos in datasset:
- "Pinot Gris" is white wine
- * "Carnet Franc" does not exist, "Cabernet France" does

Split red and white ones
- you can plot twice (set the color for two different plots)
- Can use seaborn?

Main:
Currently, main is used as sergeant and main interface
- I need to convert dump.json to a numpy array and feed that to the plot

Athena.py pings Athena on AWS with a specific SQL search
- The output can be sent to the file "raw data"
- Output can also be assigned to a json var

jsonparsing.py reads a dictionary akin to the Athena output and outputs a cleaned up json file called dump.json
- it should follow Athena
