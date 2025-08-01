from script import threshold_df
import pandas as pd


def test_threshold_df():
    # test with synth data below threshold, threshold to 5 rows
    df_1 = pd.DataFrame([[0, 1], [0, 1]], columns=["col1", "col2"])
    df_2 = pd.DataFrame(
        [[0, 1], [0, 1], [None, None], [None, None], [None, None]],
        columns=["col1", "col2"],
    )
    assert df_2.equals(threshold_df(df_1, threshold=5))

    # test with synth data above threshold, threshold to 2 rows
    df_3 = pd.DataFrame(
        [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]], columns=["col1", "col2"]
    )
    df_4 = pd.DataFrame([[0, 1], [0, 1]], columns=["col1", "col2"])
    assert df_4.equals(threshold_df(df_3, threshold=2))
