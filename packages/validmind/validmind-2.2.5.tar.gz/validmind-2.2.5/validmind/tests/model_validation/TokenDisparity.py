# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

import pandas as pd
import plotly.graph_objects as go

from validmind import tags, tasks


@tags("nlp", "text_data", "visualization")
@tasks("text_classification", "text_summarization")
def TokenDisparity(dataset, model):
    """
    Evaluates the token disparity between reference and generated texts, visualizing the results through histograms
    and bar charts, alongside compiling a comprehensive table of descriptive statistics for token counts.

    **Purpose:**
    This function is designed to assess the token disparity between reference and generated texts. Token disparity is
    important for understanding how closely the length and token usage of generated texts match the reference texts.

    **Test Mechanism:**
    The function starts by extracting the true and predicted values from the provided dataset and model. It then calculates
    the number of tokens in each reference and generated text. Histograms and bar charts are generated for the token counts
    of both reference and generated texts to visualize their distribution. Additionally, a table of descriptive statistics
    (mean, median, standard deviation, minimum, and maximum) is compiled for the token counts, providing a comprehensive
    summary of the model's performance.

    **Signs of High Risk:**
    - Significant disparity in token counts between reference and generated texts could indicate issues with text generation
      quality, such as verbosity or lack of detail.
    - Consistently low token counts in generated texts compared to references might suggest that the model is producing
      incomplete or overly concise outputs.

    **Strengths:**
    - Provides a simple yet effective evaluation of text length and token usage.
    - Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of token counts.
    - Descriptive statistics offer a concise summary of the model's performance in generating texts of appropriate length.

    **Limitations:**
    - Token counts alone do not provide a complete assessment of text quality and should be supplemented with other metrics and qualitative analysis.
    """

    # Extract true and predicted values
    y_true = dataset.y
    y_pred = dataset.y_pred(model)

    # Calculate token counts
    token_counts_true = [len(text.split()) for text in y_true]
    token_counts_pred = [len(text.split()) for text in y_pred]

    # Create a dataframe for reference and generated token counts
    df = pd.DataFrame(
        {"reference_tokens": token_counts_true, "generated_tokens": token_counts_pred}
    )

    figures = []

    # Generate histograms and bar charts for reference and generated token counts
    token_types = ["reference_tokens", "generated_tokens"]
    token_names = ["Reference Tokens", "Generated Tokens"]

    for token_type, token_name in zip(token_types, token_names):
        # Histogram
        hist_fig = go.Figure(data=[go.Histogram(x=df[token_type])])
        hist_fig.update_layout(
            title=f"{token_name} Histogram",
            xaxis_title=token_name,
            yaxis_title="Count",
        )
        figures.append(hist_fig)

        # Bar Chart
        bar_fig = go.Figure(data=[go.Bar(x=df.index, y=df[token_type])])
        bar_fig.update_layout(
            title=f"{token_name} Bar Chart",
            xaxis_title="Row Index",
            yaxis_title=token_name,
        )
        figures.append(bar_fig)

    # Calculate statistics for each token count type
    stats_df = df.describe().loc[["mean", "50%", "max", "min", "std"]]
    stats_df = stats_df.rename(
        index={
            "mean": "Mean Count",
            "50%": "Median Count",
            "max": "Max Count",
            "min": "Min Count",
            "std": "Standard Deviation",
        }
    ).T
    stats_df["Count"] = len(df)

    # Rename columns for clarity
    stats_df.index = stats_df.index.map(
        {"reference_tokens": "Reference Tokens", "generated_tokens": "Generated Tokens"}
    )

    # Create a DataFrame from all collected statistics
    result_df = pd.DataFrame(stats_df).reset_index().rename(columns={"index": "Metric"})

    return (result_df, *tuple(figures))
