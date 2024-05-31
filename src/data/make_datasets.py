import pandas as pd
import json

def load_data(url):
    return clean_data(pd.read_parquet(url,engine="pyarrow"))

def clean_data(df):
    for column in df.columns:
        if df[column].dtype == object:
            try:
                df[column] = df[column].apply(lambda x: json.loads(x.replace("'", "\""))['Utilidad Neta'] if pd.notna(x) else x)
            except (json.JSONDecodeError, KeyError):
                continue

    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    df.drop_duplicates(inplace=True)

    return df

def merge_dataframes():
    arrears_adj = load_data('https://drive.google.com/uc?export=download&id=1Pcl-Jpvu1Ixtl-rDHY2o8Vdy63g4aEC9')
    eeff = load_data('https://drive.google.com/uc?export=download&id=1fTo2b_ReZ8eVzm76kQIlOy62teTQsxVT')
    hist_loans = load_data('https://drive.google.com/uc?export=download&id=1m8H_sTubphMaU0CH625LrPHXYNHAMN96')
    merged_loans_arrears = pd.merge(hist_loans, arrears_adj, left_on='LOAN_CODE', right_on='LOAN_CODE', how='inner')
    eeff['CLIENT_ID'] = eeff['CLIENT_ID'].astype('int64')
    final_merged_df = pd.merge(merged_loans_arrears, eeff, on='CLIENT_ID', how='inner')
    final_merged_df = final_merged_df[['CLIENT_ID', 'ARREARS_DAYS', 'LOAN_CODE','ARREARS_DATE','ACTIVATION_DATE']]
    
    return final_merged_df

def yearly_count_dataframe(df):
    df['YEAR'] = df['ARREARS_DATE'].dt.year
    yearly_counts_df = df.groupby('YEAR').size().reset_index(name='Count of Arrears')
    yearly_counts_df = df.groupby('YEAR').size().reset_index(name='COUNT')
    return yearly_counts_df

def get_trainnig_model_dataframe(df):  
    df['default'] = (df['ARREARS_DAYS'] > 30).astype(int)
    df['rolling_arrears_mean'] = df.groupby('CLIENT_ID')['ARREARS_DAYS'].transform(lambda x: x.rolling(window=6, min_periods=1).mean())
    df = df[['CLIENT_ID', 'ARREARS_DAYS', 'LOAN_CODE','ARREARS_DATE','ACTIVATION_DATE','rolling_arrears_mean','default']]
    return df