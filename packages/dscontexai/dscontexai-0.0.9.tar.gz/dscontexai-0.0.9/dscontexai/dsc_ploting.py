import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set visualization styles
sns.set_theme(style="white", font_scale=2.5)
sns.set_palette("deep")
sns.set_context("paper")

plt.rcParams["xtick.bottom"] = True
plt.rcParams["ytick.left"] = True
plt.rcParams["font.family"] = "serif"
plt.rcParams["axes.labelsize"] = 18
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
plt.rcParams["axes.facecolor"] = "w"
plt.rc("font", weight="bold")


def plot_shap(shap_values: list, feature_values: list, fig_path: str) -> None:
    """
    Plot SHAP values for a given instance.

    Parameters
    ----------
    shap_values : list
        SHAP values for the instance.
    feature_values : list
        Feature values for the instance.
    fig_path : str
        Path to save the plot.

    Returns
    -------
    None
    """

    for index, item in enumerate(shap_values):
        new = round(item, 2)

        if new == 0:
            new = item

        shap_values[index] = new

    # Sort features by absolute SHAP value
    sorted_indices = sorted(
        range(len(shap_values)), key=lambda k: abs(shap_values[k]), reverse=True
    )
    sorted_features = [feature_values[i] for i in sorted_indices]
    sorted_shap_values = [shap_values[i] for i in sorted_indices]

    limit = 8
    if len(sorted_shap_values) > limit:
        sorted_shap_values = np.append(sorted_shap_values[:limit], sum(sorted_shap_values[limit:]))
        sorted_features = sorted_features[:limit]
        sorted_features.append("Other")

    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = sns.barplot(
        x=sorted_shap_values, y=sorted_features, color="gray", edgecolor="black", ax=ax
    )

    for i, (bar, val) in enumerate(zip(bars.patches, sorted_shap_values)):
        if abs(val) < 0.05:
            text_color = "black"
            ha_alignment = "right" if val < 0 else "left"
            offset = 0.005 if val > 0 else -0.005
        else:
            text_color = "white"
            ha_alignment = "left" if val < 0 else "right"
            offset = 0.005 if val < 0 else -0.005

        val_str = f"{val:+.2f}"
        ax.text(
            val + offset,
            i,
            r"\textbf{{{val_str}}}".format(val_str=val_str),
            va="center",
            ha=ha_alignment,
            color=text_color,
            fontsize=16,
            weight="bold",
        )

    # Customize the plot
    ax.set_xlabel(r"\textbf{SHAP values}", fontsize=24, weight="bold")
    ax.set_ylabel(r"\textbf{Person characteristics}", fontsize=24, weight="bold")

    # Adding grid lines for better readability
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, color="grey", axis="x")
    # Set line at 0 to be strong black
    ax.axvline(x=0, color="black", linewidth=1.5)

    # Enhancing the ticks
    ax.tick_params(axis="x", labelsize=20, width=1.5)
    ax.tick_params(axis="y", labelsize=20, width=1.5)

    # remove y axis ticks
    ax.yaxis.set_ticks_position("none")

    # set xlim to the range of the SHAP values
    ax.set_xlim(min(sorted_shap_values) - 0.05, max(sorted_shap_values) + 0.05)

    # Adding a border around the plot
    for spine in ["top", "right", "bottom", "left"]:
        ax.spines[spine].set_color("0.5")
        ax.spines[spine].set_visible(True)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_linewidth(1.2)

    fig.tight_layout()

    if os.path.exists(fig_path):
        os.remove(fig_path)

    fig.savefig(fig_path, format="pdf")
