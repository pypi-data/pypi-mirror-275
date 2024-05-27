import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier as XGBClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame) -> tuple:
    df["gender"] = df["gender"].astype("category").cat.codes
    df = df[df["smoking_history"] != "No Info"]
    smoker_status = ["current", "ever", "former"]
    df["smoking_history"] = df["smoking_history"].apply(lambda x: 1 if x in smoker_status else 0)

    X = df.drop(columns=["diabetes"])
    y = df["diabetes"]

    return X, y


def train_model(X: pd.DataFrame, y: pd.Series) -> XGBClassifier:
    model = XGBClassifier()
    model.fit(X, y)

    pickle.dump(model, open("./models/model.pkl", "wb"))
    return model


def predict(model: XGBClassifier, X: pd.DataFrame) -> np.ndarray:
    return model.predict(X)


if __name__ == "__main__":
    _is_trained = False
    data = load_data("kaggle_data/diabetes_prediction_dataset_balanced.csv")

    X, y = preprocess_data(data)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if not _is_trained:
        clf = train_model(X_train, y_train)
    else:
        clf = pickle.load(open("./models/diabetes_model.pkl", "rb"))

    y_pred = predict(clf, X_test)
