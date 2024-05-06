import pandas as pd
from life_expectancy.load_save import load_data, save_data
from . import FIXTURES_DIR

def test_save_data():
    pass

def test_load_data(eu_life_expectancy_raw_sample):
    data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv")
    pd.testing.assert_frame_equal(
        data, eu_life_expectancy_raw_sample
    )