# Script for creating new features
import pandas as pd


def create_features(df):
    """
    Creates tendencies dataframe based on arrears of clients(6 months)

    Parameters:
    df (pd.DataFrame): Data frame containing the original data.

    Returns:
    pd.DataFrame: Data frame with new column added max_arrears_6m with tendency calculations on it.
    """
    # Getting Max arrears days over the last 6 months and we're creating and new row into the dataframe
    df['max_arrears_6m'] = df['arrears_days'].rolling(window=180).max()
    return df
