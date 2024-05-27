import argparse
import json
import pickle

import pandas as pd
import shap
from catboost import CatBoostClassifier

from dscontexai.dsc_grammar import analyze_shap_values


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


def general(model_path, dataset_path, config, idx):
    """
    Load the insurance model and data, and generate a report for a specific instance.
    """

    df = pd.read_csv(dataset_path)
    X = df.drop(columns=["diabetes"])
    y = df["diabetes"]

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

    explainer = shap.Explainer(model, X, model_output="probability")
    shap_values_array = explainer(X.iloc[idx])

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

    parser.add_argument("--domain", help="Dataset domain", action="store", default="diabetes")
    parser.add_argument("--instance", help="Instance index", action="store", default=1, type=int)
    parser.add_argument("--model", help="Model path", action="store", default=None)
    parser.add_argument("--dataset", help="Data path", action="store", default=None)
    parser.add_argument("--config", help="Config path", action="store", default=None)
    parser.add_argument("--index", help="Instance index", action="store", default=1, type=int)

    args = parser.parse_args()

    if args.index < 0:
        print("Index has to be positive!")
        exit()
    if args.domain not in ["diabetes", "insurance"]:
        print("Invalid domain. Please enter either 'diabetes' or 'insurance'.")
        exit()

    if args.domain == "diabetes":
        model_path = "./models/diabetes_model.pkl"
        df = pd.read_csv("./kaggle_data/processed_data.csv")
        diabetes_case()
    elif args.domain == "insurance":
        model_path = "../../malaysia_churn_model/model/gigt_model_exp1.bin"
        df = pd.read_csv("../../malaysia_churn_model/data/data_sample.csv", index_col=0)
        insurance_case()
    elif args.domain == "general":
        model_path = args.model
        data = args.dataset
        config = args.config
        general(model_path, data, config, args.index)
    else:
        print("Invalid domain. Please enter either 'diabetes', 'insurance' or 'general'.")
        exit()
