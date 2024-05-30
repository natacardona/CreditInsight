# Script for creating new features
import pandas as pd


def create_features(df):
    # Ensure the data is sorted by date if necessary
    df.sort_values(by=['CLIENT_ID', 'ARREARS_DATE'], inplace=True)

    # Set the index to the date for rolling calculation
    df.set_index('ARREARS_DATE', inplace=True)

    # Group by 'CLIENT_ID' and apply a rolling window of 6 months to calculate the max arrears days
    df['max_arrears_6m'] = df.groupby('CLIENT_ID')['ARREARS_DAYS'].rolling('180D').max().reset_index(level=0, drop=True)
    
    # Reset index after operations
    df.reset_index(inplace=True)
   
    # Select only the columns you want to keep
    df = df[['CLIENT_ID', 'ARREARS_DAYS', 'max_arrears_6m','ARREARS_DATE']]
    
    return df
