
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_categorical_data(df_model):
    
    df_model.loc[:, 'ARREARS_DATE'] = pd.to_datetime(df_model['ARREARS_DATE'])
    df_model.loc[:, 'ACTIVATION_DATE'] = pd.to_datetime(df_model['ACTIVATION_DATE'])
    df_model.loc[:, 'days_since_activation'] = (df_model['ARREARS_DATE'] - df_model['ACTIVATION_DATE']).dt.days
    X = df_model[['ARREARS_DAYS', 'rolling_arrears_mean', 'days_since_activation']]
    y = df_model['default']
    return X,y
    
def prepare_training_sets(df_model): 
    X, y = prepare_categorical_data(df_model)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return  X_train, X_test, y_train, y_test,X
  
