import argparse
import json
import pickle

import pandas as pd
import shap
from catboost import CatBoostClassifier
from dsc_grammar import analyze_shap_values


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
    import json

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


def insurance_case() -> None:
    """
    Load the insurance model and data, and generate a report for a specific instance.
    """

    df = pd.read_csv("../../malaysia_churn_model/data/data_sample.csv", index_col=0)

    # Load churn prediction model
    model = CatBoostClassifier()
    model.load_model("../../malaysia_churn_model/model/gigt_model_exp1.bin")

    # Expert descriptions for values below, within, and above optimal ranges
    # read from json file
    with open("./configurations/insurance.json") as f:
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

    explainer = shap.KernelExplainer(model.predict_proba, shap.sample(df, 5))
    shap_values_array = explainer(df.iloc[index])

    shap_values_array.values = shap_values_array.values[:, 1]
    shap_values_array.base_values = shap_values_array.base_values[1]

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Report Generator for xAI")

    parser.add_argument("--domain", help="Dataset domain", action="store", default="diabetes")

    args = parser.parse_args()

    if args.domain == "diabetes":
        diabetes_case()
    elif args.domain == "insurance":
        insurance_case()
    else:
        print("Invalid domain. Please enter either 'diabetes' or 'insurance'.")
