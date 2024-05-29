import pandas as pd


def load_data(url):
    """
    Load data from a Parquet file into a pandas DataFrame.

    Parameters:
    url (str): The path to the Parquet file.

    Returns:
    pd.DataFrame: Data loaded into a pandas DataFrame.
    """
    return pd.read_parquet(url,engine="pyarrow")