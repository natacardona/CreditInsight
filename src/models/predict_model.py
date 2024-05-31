import pandas as pd


def interpret_results(model,X):
    feature_importance = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_[0]})
    print(feature_importance.sort_values(by='Coefficient', ascending=False))