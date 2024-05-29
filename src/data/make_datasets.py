# Script for loading and cleaning data
import pandas as pd
import json

def load_data(url):
    """
    Load data from a Parquet file into a pandas DataFrame.

    Parameters:
    url (str): The path to the Parquet file.

    Returns:
    pd.DataFrame: Data loaded into a pandas DataFrame.
    """
    return clean_data(pd.read_parquet(url,engine="pyarrow"))

def clean_data(df):
    """
    Perform data cleaning operations such as filling missing values and removing duplicates.
    Also handles columns with JSON-like strings by parsing them.

    Parameters:
    df (pd.DataFrame): The data frame to clean.

    Returns:
    pd.DataFrame: The cleaned data frame.
    """
    for column in df.columns:
        # Try to detect if the column contains JSON-like strings
        if df[column].dtype == object:
            try:
                # If the column can be converted to JSON, extract a specific value
                # This example assumes you want to extract 'Utilidad Neta' from the JSON
                df[column] = df[column].apply(lambda x: json.loads(x.replace("'", "\""))['Utilidad Neta'] if pd.notna(x) else x)
            except (json.JSONDecodeError, KeyError):
                # If there's an error in parsing JSON or the key doesn't exist, keep the original
                continue

    # Now handle numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df