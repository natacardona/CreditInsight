
# Script for training and saving models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_predict(df, target):
    """
    Train a model and predict the target variable.

    Parameters:
    df (pd.DataFrame): The data frame containing features.
    target (str): The name of the target variable.

    Returns:
    dict: A dictionary containing the model and performance metrics.
    """
    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))
    return {'model': model, 'report': classification_report(y_test, predictions, output_dict=True)}
