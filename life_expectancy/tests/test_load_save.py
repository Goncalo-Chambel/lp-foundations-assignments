import pandas as pd
from life_expectancy.load_save import load_data, save_data
from unittest.mock import patch
from . import FIXTURES_DIR, DATA_DIR

def test_save_data():
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:

        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        print(df)
        save_data(df, "dummy_data.csv")
        mock_to_csv.assert_called_once_with("dummy_data.csv", index=False)

def test_load_data(eu_life_expectancy_raw_sample):
    data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv")
    pd.testing.assert_frame_equal(
        data, eu_life_expectancy_raw_sample
    )