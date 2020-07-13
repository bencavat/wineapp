import matplotlib.pyplot as plt
import numpy as np
from wineapp.Athena import submit_query
from wineapp.Athena import get_query_results
from wineapp.jsonparsing import dump_clean_data
from wineapp.jsonparsing import turn_data_into_array

import boto3


client = boto3.client('athena')
query = "SELECT * FROM wine WHERE acidity >= 2"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"
clean_file = "dump.csv"


class ReturnedWines:
    pass


def plot_wines(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set(xlabel='Acidity', ylabel='Body',
           title='My wines')
    ax.grid()

    plt.show()
    # Artists


def main():
    response = submit_query(query, database, s3_output)
    results = get_query_results(response)
    #[save_results(results, savefile) if results else print("No results, no savefile")]
    print(results)
    dump_clean_data(results["ResultSet"]["Rows"], clean_file)
    print(results)
    acidity, body = turn_data_into_array(results["ResultSet"]["Rows"])
    print(f'acidity is {acidity}')
    print(f'body is {body}')
    plot_wines(acidity, body)


if __name__ == "__main__":
    main()