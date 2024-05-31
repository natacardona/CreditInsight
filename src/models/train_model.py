import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from models.model import prepare_training_sets
from models.predict_model import interpret_results


def train_model(df):
    X_train, X_test, y_train, y_test,X = prepare_training_sets(df)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)
    evaluate_model(model,X_test_scaled,y_test)
    interpret_results(model,X)

def evaluate_model(model,X_test_scaled,y_test):
    y_pred_prob = model.predict_proba(X_test_scaled)[:, 1]  # Get probabilities for the positive class
    y_pred = model.predict(X_test_scaled)  # Get class predictions

    # Metrics
    auc_score = roc_auc_score(y_test, y_pred_prob)
    print(f'AUC Score: {auc_score}')
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


