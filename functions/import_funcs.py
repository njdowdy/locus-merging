import pandas as pd


def import_data(my_csv):
    df = pd.read_csv(my_csv)
    return df
