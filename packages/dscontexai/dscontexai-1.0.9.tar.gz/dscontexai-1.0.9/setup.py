from setuptools import find_packages, setup

VERSION = "1.0.9"
DESCRIPTION = "Contextualizing model's decisions with natural language explanations."
LONG_DESCRIPTION = """
# ConteXAI - Contextualizing model's decisions with natural language explanations

ConteXAI is a Python package developed as part of the Data Science Project Competition 2024. 

The library **links local explainability methods with natural language explanations**, allowing users to gain detailed insights into model predictions.
By incorporating additional domain knowledge, users can obtain even better insights into the model's predictions.

### Install

ConteXAI can be installed using pip:
```bash
pip install dscontexai
```

### Generate XAI reports

Using this library, you can fully automatically develop your XAI reports. Currently, it supports SHAP values, which is a local feature importance measure, to which we added textual explanations and domain-related context.
The library can be used for binary classification problems, for all models that output probabilities.

The report consists of four main segments: 

  (1) Description of local feature importances, 

  (2) Explanation of the instance's prediction, 

  (3) Visualization of local feature importances, 
  
  (4) Explanation of the visualization in natural language and context related to the domain and the prediction. 

<p align="center">
  <img src="https://raw.githubusercontent.com/jovanavidenovic/ConteXAI/main/other/XAI_2_page-0001.jpg" alt="Report structure" width="85%">
</p>

### Preparing configuration file
To use this tool with your model and dataset, you need to provide a configuration JSON file for a dataset, structured like the one below.

```bash
{
  # domain-based context
  "optimal_values": [
  ...
    [0, 6.5],               # HbA1c level optimal range is from 0 to 6.5
    [100, 140]              # Glucose level optimal range is from 100 to 140 
  ],
  "descriptions": {
    "below_optimal": [
      # Context for feature values falling below the optimal range
    ],
    "optimal": [
      # Context for feature values falling within the optimal range
    ],
    "above_optimal": [
      # Context for feature values falling above the optimal range
    ]
  },
  # Data transformations for feature mapping
  "transformation": {
    "0": ["Man", "Woman"],  # Transformation for Gender
    "1": [],                # No transformation for Age (numeric)
    "2": ["No", "Yes"],     # Transformation for Hypertension
    ...
  },
  "feature_names": [
    "Gender",
    "Age",
    "Hypertension",
    "Heart_disease",
    "Smoking_history",
    "BMI",
    "HbA1c_level",
    "Blood_glucose_level"
  ],
  # variables needed for structuring the description
  "target1": "diabetes",    # Target variable the model is predicting
  "target2": "Person",      # The object representing a sample in a data
  "supporting": ["does", "have"]  # Supporting verbs used in descriptions
}
```

#### Running the generation
Once you have model, dataset, and config file ready, to generate the report, you can use the following code snippet:
  
  ```python
  from dscontexai.generate_report import general

  general.generate_report(model_path= "path/to/model.pkl", dataset_path="path/to/data.csv", config="path/to/config.json", idx=sample_idx)
  ```

After successful generation, you will find a PDF report in the directory prototype/ under the name output_{sample_idx}.pdf.

#### Example notebooks

Working example, as well as the example of the generated report and the configuration file, can be found [here](https://github.com/jovanavidenovic/ConteXAI/tree/main/titanic).
 
#### Examples
Examples of the generated reports are shown below. Problem domain was diabetes prediction.

![Example 1](https://raw.githubusercontent.com/jovanavidenovic/ConteXAI/main/other/output_10_page-0001.jpg)
![Example 2](https://raw.githubusercontent.com/jovanavidenovic/ConteXAI/main/other/output_4130_page-0001.jpg)
"""

# Setting up
setup(
    name="dscontexai",
    version=VERSION,
    author="Jovana V., Haris K., Luka M.",
    author_email="hk8302@student.uni-lj.si",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={"dscontexai": ["latex/neurips_2023.sty"]},
    install_requires=[
        "asttokens==2.4.1",
        "backcall==0.2.0",
        "catboost==1.2.5",
        "cloudpickle==3.0.0",
        "comm==0.2.2",
        "contourpy==1.1.1",
        "cycler==0.12.1",
        "debugpy==1.8.1",
        "decorator==5.1.1",
        "executing==2.0.1",
        "fonttools==4.51.0",
        "graphviz==0.20.3",
        "importlib-metadata==7.1.0",
        "importlib-resources==6.4.0",
        "ipykernel==6.29.4",
        "ipython==8.12.3",
        "jedi==0.19.1",
        "joblib==1.4.0",
        "jupyter-client==8.6.1",
        "jupyter-core==5.7.2",
        "kiwisolver==1.4.5",
        "llvmlite==0.41.1",
        "matplotlib==3.7.5",
        "matplotlib-inline==0.1.7",
        "nest-asyncio==1.6.0",
        "numba==0.58.1",
        "numpy==1.24.4",
        "ordered-set==4.1.0",
        "packaging==24.0",
        "pandas==2.0.3",
        "parso==0.8.4",
        "pexpect==4.9.0",
        "pickleshare==0.7.5",
        "pillow==10.3.0",
        "platformdirs==4.2.0",
        "plotly==5.22.0",
        "prompt-toolkit==3.0.43",
        "psutil==5.9.8",
        "ptyprocess==0.7.0",
        "pure-eval==0.2.2",
        "pygments==2.17.2",
        "PyLaTeX==1.4.2",
        "pyparsing==3.1.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.1",
        "pyzmq==26.0.0",
        "scikit-learn==1.3.2",
        "scipy==1.10.1",
        "seaborn==0.13.2",
        "shap==0.44.1",
        "six==1.16.0",
        "slicer==0.0.7",
        "stack-data==0.6.3",
        "tenacity==8.3.0",
        "threadpoolctl==3.4.0",
        "tornado==6.4",
        "tqdm==4.66.2",
        "traitlets==5.14.2",
        "typing-extensions==4.11.0",
        "tzdata==2024.1",
        "xgboost==2.0.3",
        "wcwidth==0.2.13",
        "zipp==3.18.1",
    ],
    long_description_content_type="text/markdown",
    keywords=["python", "first package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
