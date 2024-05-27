import argparse
import json
import pickle

import pandas as pd
import shap
import xgboost as xgb
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier

from dscontexai.dsc_grammar import analyze_shap_values


def get_shap(model, X: pd.DataFrame, index: int) -> shap.Explainer:
    if isinstance(model, xgb.XGBClassifier):
        explainer = shap.Explainer(model, X, model_output="probability")
        shap_values = explainer(X.iloc[index])
    else:
        explainer = shap.KernelExplainer(model.predict_proba, shap.sample(X, 1000))
        shap_values = explainer(X.iloc[index])
        if shap_values.values.shape[1] == 2:
            shap_values.values = shap_values.values[:, 1]
            shap_values.base_values = shap_values.base_values[:, 1][0]

    return shap_values


def diabetes_case() -> None:
    """
    Load the diabetes model and data, and generate a report for a specific instance.
    """
    df = pd.read_csv("./kaggle_data/processed_data.csv")
    X = df.drop(columns=["diabetes"])
    y = df["diabetes"]

    with open("./models/diabetes_model.pkl", "rb") as f:
        model = pickle.load(f)

    # Expert descriptions for values below, within, and above optimal ranges
    # read from json file
    with open("configurations/diabetes.json") as f:
        data = json.load(f)

    optimal_values = data["optimal_values"]
    below_optimal_descriptions = data["descriptions"]["below_optimal"]
    optimal_descriptions = data["descriptions"]["optimal"]
    above_optimal_descriptions = data["descriptions"]["above_optimal"]

    transformations = data["transformation"]

    feature_names = data["feature_names"]
    target1 = data["target1"]
    target2 = data["target2"]
    supporting = data["supporting"]
    index = data["index"]

    explainer = shap.Explainer(model, X, model_output="probability")
    shap_values_array = explainer(X.iloc[index])

    analyze_shap_values(
        shap_values_array,
        index,
        target1,
        target2,
        feature_names,
        supporting,
        optimal_values,
        below_optimal_descriptions,
        optimal_descriptions,
        above_optimal_descriptions,
        transformations,
    )


def general(model_path, dataset_path, config, idx):
    """
    Load the insurance model and data, and generate a report for a specific instance.
    """

    # Load prediction model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Expert descriptions for values below, within, and above optimal ranges
    # read from json file
    with open(config) as f:
        data = json.load(f)

    optimal_values = data["optimal_values"]
    below_optimal_descriptions = data["descriptions"]["below_optimal"]
    optimal_descriptions = data["descriptions"]["optimal"]
    above_optimal_descriptions = data["descriptions"]["above_optimal"]

    transformations = data["transformation"]

    feature_names = data["feature_names"]
    target1 = data["target1"]
    target2 = data["target2"]
    supporting = data["supporting"]

    df = pd.read_csv(dataset_path)
    X = df.drop(columns=[target1])
    y = df[target1]

    shap_values_array = get_shap(model, X, idx)

    analyze_shap_values(
        shap_values_array,
        idx,
        target1,
        target2,
        feature_names,
        supporting,
        optimal_values,
        below_optimal_descriptions,
        optimal_descriptions,
        above_optimal_descriptions,
        transformations,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Report Generator for xAI")

    parser.add_argument("--instance", help="Instance index", action="store", default=1, type=int)
    parser.add_argument("--model", help="Model path", action="store", default=None)
    parser.add_argument("--dataset", help="Data path", action="store", default=None)
    parser.add_argument("--config", help="Config path", action="store", default=None)
    parser.add_argument("--index", help="Instance index", action="store", default=1, type=int)
    parser.add_argument(
        "--example",
        help="Shows working example of the library",
        action="store_true",
        required=False,
    )

    args = parser.parse_args()

    if args.index < 0:
        print("Index has to be positive!")
        exit()

    if args.example:
        model_path = "./models/diabetes_model.pkl"
        df = pd.read_csv("./kaggle_data/processed_data.csv")
        diabetes_case()
    else:
        model_path = args.model
        data = args.dataset
        config = args.config
        general(model_path, data, config, args.index)
