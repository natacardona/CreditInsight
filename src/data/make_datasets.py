# Script for loading and cleaning data
import pandas as pd
import json
import numpy as np
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

def merge_dataframes():
    
    arrears_adj = load_data('https://drive.google.com/uc?export=download&id=1Pcl-Jpvu1Ixtl-rDHY2o8Vdy63g4aEC9')
  
    eeff = load_data('https://drive.google.com/uc?export=download&id=1fTo2b_ReZ8eVzm76kQIlOy62teTQsxVT')
    
    hist_loans = load_data('https://drive.google.com/uc?export=download&id=1m8H_sTubphMaU0CH625LrPHXYNHAMN96')
    
    # Assuming hist_loans, eeff, and arrears_adj are already loaded as DataFrames
    merged_loans_arrears = pd.merge(hist_loans, arrears_adj, left_on='LOAN_CODE', right_on='LOAN_CODE', how='inner')
    
    # Convert CLIENT_ID in eeff to int64 if necessary
    eeff['CLIENT_ID'] = eeff['CLIENT_ID'].astype('int64')

    # Merge the previously merged data with eeff
    final_merged_df = pd.merge(merged_loans_arrears, eeff, on='CLIENT_ID', how='inner')
    
    return final_merged_df