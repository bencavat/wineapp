def request_varietal():
    requested_wines = input("Enter the wine(s) you're looking for separated by a comma.")
    varietal_query = f"SELECT * FROM wine WHERE name IN ('{requested_wines}');"
    print(varietal_query)


def request_attributes():
    requested_attributes = input("Right now we only hone the search by acidity, body, and color. "
                                 "\n\nWhat do you want?")

    attribute_query = f"SELECT * FROM wine WHERE"



def get_request():
    yes_synonyms = ["y", "yes", "yeah", "yep", "si", "oui"]
    want_varietal = input("Do you have a specific wine in mind?")
    if want_varietal in yes_synonyms:
        print("Okay, let's find that wine!")
        request_varietal()
    else:
        print("Ok, how about we search by attribute?")
        request_attributes()


if __name__ == "__main__":
    get_request()
