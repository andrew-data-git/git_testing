import pandas as pd
import numpy as np
import json
import csv
import requests
import logging


def extract_csv(filepath):
    """Read a csv into a pandas dataframe."""
    df = pd.read_csv(filepath)
    return df


def extract_json(filepath):
    """Read a csv into a pandas dataframe."""
    df = pd.read_json(filepath)
    return df


def threshold_df(df, threshold=5):
    """For a given df, cut it to 10 lines long, otherwise pad it to ten lines with nulls.

    Args:
        df (pd.DataFrame): the df to transform
        threshold (int): lines to coerce df to

    Returns:
        df: transformed result
    """
    line_count = df.shape[0]
    if line_count >= threshold:
        return df.head(threshold)
    else:
        pad_df = pd.DataFrame(
            np.nan,
            index=range(line_count, threshold, 1),
            columns=df.columns,
        )
        return pd.concat([df, pad_df], axis=0, ignore_index=True)


if __name__ == "__main__":
    # pull data
    csv_df = extract_csv("data.csv")
    json_df = extract_json("data.json")

    # transform to match requirement
    csv_t = threshold_df(csv_df)
    json_t = threshold_df(json_df, threshold=10)

    # load
    print(csv_t)
    print(json_t)
