import matplotlib.pyplot as plt
import numpy as np
from wineapp.Athena import submit_query
from wineapp.Athena import get_query_results
from wineapp.jsonparsing import dump_clean_data
import boto3


client = boto3.client('athena')
query = "SELECT * FROM wine WHERE acidity >= 2"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"
json_file = "dump.json"


class ReturnedWines:
    pass


def plot_wines():
    fig = plt.figure()
    ax = fig.add_subplot()
    # Artists
    ax.set_title("Wines")
    ax.set_xlabel('Acidity')
    ax.set_ylabel('Body')
    ax.plot([1,2,3], [3,2,1])

    plt.show()


def main():
    response = submit_query(query, database, s3_output)
    results = get_query_results(response)
    #[save_results(results, savefile) if results else print("No results, no savefile")]
    dump_clean_data(results["ResultSet"]["Rows"], json_file)
    plot_wines()


if __name__ == "__main__":
    main()