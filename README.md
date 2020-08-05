# wineapp
wine repo

To do:

Words to SQL:
- create FST?
  - https://pypi.org/project/openfst-python/
  - http://www.opengrm.org/twiki/bin/view/GRM/PyniniDocs
- ML model
  - come up with a bunch of examples (building annotated training data set)
    - "a red|Color wine with high|AcidityValue acidity|Acidity"
    - "a white|Color wine with high|BodyValue body|Body"
    - could compile list of many synonyms for body, acidity
  - information extraction model: every single token is labeled, narrows

Fix typos in dataset:
- "Pinot Gris" is white wine
- * "Carnet Franc" does not exist, "Cabernet France" does

Plotting wines
- Can use seaborn?

######

To done:
Athena.py pings Athena on AWS with a specific SQL search
- The output can be sent to the file "raw data"
- Output can also be assigned to a json var

jsonparsing.py reads a dictionary akin to the Athena output and outputs a cleaned up json file called dump.json
- it should follow Athena
