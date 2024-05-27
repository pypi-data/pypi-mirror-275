import os

import matplotlib.pyplot as plt
import numpy as np
import pkg_resources
import shap
from pylatex import Document, Figure, Itemize, NoEscape, Package, Section, Subsection
from pylatex.utils import bold

from dscontexai.dsc_ploting import plot_shap

plt.rcParams["text.usetex"] = True


def fixing_variable_names(variables: list) -> list:
    """
    Fix the variable names by removing underscores and capitalizing the first letter of each word.

    Parameters
    ----------
    variables : list
        List of variable names.

    Returns
    -------
    list
        List of fixed variable names.
    """

    fixed_names = []
    for var in variables:
        # Remove underscores and capitalize the first letter of each word
        fixed_name = var.replace("_", " ")
        # Capitalize the first letter of the first word
        fixed_name = fixed_name[0].upper() + fixed_name[1:]
        fixed_names.append(fixed_name)

    return fixed_names


def fix_feature_values(feature_values: list) -> list:
    """
    Fix the feature values by rounding them to 2 decimal places.

    Parameters
    ----------
    feature_values : list
        List of feature values.

    Returns
    -------
    list
        List of fixed feature values.
    """

    fixed_values = []

    for value in feature_values:
        value = int(value) if value.is_integer() else value
        fixed_values.append(value)

    return fixed_values


def check_values(
    data: list,
    optimal_values: list,
    below_optimal_descriptions: list,
    optimal_descriptions: list,
    above_optimal_descriptions: list,
) -> list:
    """
    Check the values of the instance against the optimal values.

    Parameters
    ----------
    data : list
        List of feature values.
    optimal_values : list
        List of optimal value ranges.
    below_optimal_descriptions : list
        List of descriptions for values below the optimal range.
    optimal_descriptions : list
        List of descriptions for values within the optimal range.

    Returns
    -------
    list
        List of descriptions for each feature value.
    """

    results = []
    for (low, high), value, below_desc, optimal_desc, above_desc in zip(
        optimal_values,
        data,
        below_optimal_descriptions,
        optimal_descriptions,
        above_optimal_descriptions,
    ):
        if value < low:
            results.append(below_desc)
        elif low <= value <= high:
            results.append(optimal_desc)
        else:
            results.append(above_desc)

    return results


def transform_instance_values(instance_values: list, transformations: dict) -> list:
    """
    Transform the instance values based on the transformations.

    Parameters
    ----------
    instance_values : list
        List of instance values.
    transformations : dict
        Dictionary of transformations for the instance values.

    Returns
    -------
    list
        List of transformed instance values.
    """

    new_instance_values = []
    for index in range(len(transformations.values())):
        item = transformations.get(str(index))
        if len(item) == 0:
            new_instance_values.append(instance_values[index])
            continue
        value = instance_values[index]
        if isinstance(value, str):
            new_instance_values.append(instance_values[index])
        else:
            new_instance_values.append(item[instance_values[index]])
    return new_instance_values


def analyze_shap_values(
    shap_values_array: shap.Explanation,
    index: int,
    target1: str,
    target2: str,
    feature_names: list,
    supporting,
    optimal_values: list,
    below_optimal_descriptions: list,
    optimal_descriptions: list,
    above_optimal_descriptions: list,
    transformations: dict,
) -> None:
    """
    Analyze the SHAP values and create a report.

    Parameters
    ----------
    shap_values_array : list
        SHAP values for the instance.
    feature_names : list
        List of feature names.
    target1 : str
        Target class name.
    index : int
        Index of the instance.
    target2 : str
        Target class name.
    supporting : list
        Supporting words.
    optimal_values : list
        List of optimal value ranges.
    below_optimal_descriptions : list
        List of descriptions for values below the optimal range.
    optimal_descriptions : list
        List of descriptions for values within the optimal range.
    above_optimal_descriptions : list
        List of descriptions for values above the optimal range.
    transformations : list
        List of transformations for the instance values.

    Returns
    -------
    None
    """

    shap_values = shap_values_array.values
    starting_value = shap_values_array.base_values
    if type(starting_value) == np.ndarray:
        starting_value = starting_value[0]
    feature_values = shap_values_array.data

    # Sort the shap_values by their magnitude
    indices = np.argsort(np.abs(shap_values))[::-1]  # Descending order

    feature_names = fixing_variable_names(feature_names)
    feature_values = fix_feature_values(feature_values)
    instance_values = transform_instance_values(feature_values, transformations)

    # Create sorted arrays
    sorted_shap_values = shap_values[indices]
    # Round to 2 decimal places
    sorted_shap_values = sorted_shap_values.tolist()
    sorted_shap_values = [round(value, 2) for value in sorted_shap_values]
    sorted_shap_values = np.array(sorted_shap_values)
    sorted_feature_names = [feature_names[i] for i in indices]

    # Calculate the change array
    change = np.cumsum(sorted_shap_values) + round(starting_value, 2)

    if change[-1] > 0.5:
        status = supporting[0] + " " + supporting[1] if len(supporting) > 1 else ""
    else:
        status = f"{supporting[0]} not {supporting[1] if len(supporting) > 1 else ''}"

    if abs(change[-1] - 0.5) > 0.3:
        confidence = f"""The model is {bold("confident")} in its prediction, as the probability that the person {status} {target1} {bold("is close to 1")}."""
    else:
        confidence = f"""The model is not {bold("confident")} in its prediction, as the probability that the person {status} {target1} {bold("is close to 0.5")}."""

    output = f"""The inital prediction value equals average prediction {round(starting_value, 2)}. The feature that influences the final prediction the most for this example is {bold(sorted_feature_names[0])} with an importance of {bold(str(round(sorted_shap_values[0],2)))}, which changes the initial value to {bold(str(round(change[0],2)))}. 
    The second most important feature for this example is {bold(sorted_feature_names[1])} with a value of {bold(str(round(sorted_shap_values[1],2)))}. Now, the prediction amounts to {bold(str(round(change[1],2)))}. 
    The third most important feature is {bold(sorted_feature_names[2])} with an importance of {bold(str(round(sorted_shap_values[2],2)))}. This changes the prediction to {bold(str(round(change[2],2)))}.
    Other features together contribute {bold(str(round((change[len(change)-1]-change[2]),2)))}.
    The final prediction is {bold(str(round(change[len(change)-1],2)))}. Because the prediction is {bold("greater") if change[len(change)-1] > 0.5 else bold("less")} than 0.5, the model predicts that the {bold(target2.lower())} {bold(status)} {bold(target1)}. 
    {confidence}\n\n"""

    # Create the data for plotting
    feature_values_named = [
        f"{name} = {value}" for name, value in zip(feature_names, instance_values)
    ]

    # Sort features by absolute SHAP value
    sorted_indices = sorted(
        range(len(shap_values)), key=lambda k: abs(shap_values[k]), reverse=True
    )
    sorted_features = [feature_values_named[i] for i in sorted_indices]
    sorted_shap_values = [shap_values[i] for i in sorted_indices]

    # Set up the plot
    plot_shap(sorted_shap_values, sorted_features, "./plots/shap.pdf")

    doc = Document(documentclass="article", document_options="a4paper", page_numbers=False)
    nips_style = pkg_resources.resource_filename("dscontexai", "latex/neurips_2023.sty")
    # doc.preamble.append(NoEscape(r"\usepackage{../latex/neurips_2023}"))
    doc.preamble.append(r"\usepackage{" + nips_style + "}")
    doc.preamble.append(NoEscape(r"\usepackage{setspace}"))
    doc.packages.append(Package("graphicx"))
    doc.packages.append(Package("enumitem"))

    # Adding a section without numbering
    with doc.create(Section("Feature importance with included context and text", numbering=False)):

        # Adding a subsection
        with doc.create(Subsection("Description of the method", numbering=False)):

            doc.append(bold("Feature importance "))
            doc.append(
                "method assigns a score to each feature. Features with a higher absolute score are considered more important in predicting individual cases. The sign of the score indicates whether the feature value contributes to or argues against the prediction. The SHAP method is one of the methods of local feature importance. \n \n"
            )
            doc.append(
                bold(
                    f"The scores are visualized relative to the average prediction, which is {round(starting_value, 2)}.\n"
                )
            )
            doc.append(
                "The final prediction is equal to the sum of the average prediction and the influence of all features.\n"
            )

        # Adding another subsection
        with doc.create(
            Subsection(
                f"Predicted probability of {target1} is {change[len(change)-1]:.2f}.",
                numbering=False,
            )
        ):
            with doc.create(Figure(position="h!")) as img_:
                img_.add_image("../plots/shap.pdf", width="400px")

    doc.append(bold("\nTextual explanation: "))
    doc.append(NoEscape(output))

    # Applying the function and printing the results
    results = check_values(
        feature_values,
        optimal_values,
        below_optimal_descriptions,
        optimal_descriptions,
        above_optimal_descriptions,
    )

    doc.append(bold("\nDomain context:"))

    with doc.create(Itemize(options=["noitemsep"])) as itemize:
        for i in range(3):
            feature = sorted_feature_names[i]
            value = results[feature_names.index(feature)]
            itemize.add_item(NoEscape(f"\\textbf{{{feature}}}: {value}"))

    if not os.path.exists("./prototypes"):
        os.makedirs("./prototypes")

    doc.generate_pdf(
        os.path.join(f"./prototypes/output_{index}"),
        compiler="pdflatex",
        clean=True,
        clean_tex=True,
    )
