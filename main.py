import matplotlib.pyplot as plt
import numpy as np
from wineapp.Athena import submit_query
from wineapp.Athena import get_query_results
from wineapp.jsonparsing import dump_clean_data
from wineapp.jsonparsing import turn_data_into_array
import boto3


client = boto3.client('athena')
# query = "SELECT * FROM wine WHERE acidity >= 3 AND body>11;"
query = "SELECT * FROM wine WHERE name IN ( 'Pinot Noir', 'Sauvignon Blanc');"
database = "wine_feb_24"
s3_output = "s3://winebenathenaoutput/"
clean_file = "dump.csv"


def plot_wines(x, y, color):
    fig, ax = plt.subplots()
    whitex, whitey, redx, redy = [], [], [], []
    for c in color:
        index = color.index(c)
        [[whitex.append(x[index]), whitey.append(y[index])] if c == 'White'
        else [redx.append(x[index]), redy.append(y[index])]]
    print(f'whitex of length {len(whitex)} and whitey of length {len(whitey)}')
    print(f'redx of length {len(redx)} and redy of length {len(redy)}')
    ax.scatter(whitex, whitey, c='yellow', label='Blanc')
    ax.scatter(redx, redy, c='red', label='Rouge')
    ax.set(xlabel='Acidity', ylabel='Body', title='My wines')
    ax.grid()
    plt.legend(loc='upper left')

    plt.show()

def main():
    response = submit_query(query, database, s3_output)
    results = get_query_results(response)
    #[save_results(results, savefile) if results else print("No results, no savefile")]
    acidity, body, color = turn_data_into_array(results["ResultSet"]["Rows"][1:])
    print(f'acidity of length {len(acidity)} includes: {acidity[:5]}')
    print(f'body of length {len(body)} includes: {body[:5]}')
    print(f'color of length {len(color)} includes: {color[:5]}')
    plot_wines(acidity, body, color)


if __name__ == "__main__":
    main()