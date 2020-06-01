rawdata = ["Palomino	White	1	1", "Folle Blanche	White	1	3", "Aligoté	White	3	3"]
cleandata = []


def cleandata():
    for i in rawdata:
        data = i.split("\t")
        cleandata.append(data)

cleandata()

dictionary = {"name" : None, "color" : "red", "acidity" : None, "body" : None}

SQLrequest = f'SELECT name,\tcolor,\tbody,\tacidity' \
             f'FROM "wine_feb_24"."wine"' \
             f'WHERE acidity >= 2' \
             f'AND body = 6' \
             f'AND color = "Red"'

if color:
    SQLcolor = dictionary.get("color")
elif