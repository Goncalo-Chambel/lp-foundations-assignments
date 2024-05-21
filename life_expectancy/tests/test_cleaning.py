"""Tests for the cleaning module"""

import pandas as pd
from life_expectancy.cleaning import clean_data
from ..region import Region


def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    data_cleaned = clean_data(eu_life_expectancy_raw_sample, Region.PT).reset_index(drop=True)
    pd.testing.assert_frame_equal(
        data_cleaned, eu_life_expectancy_raw_sample_expected
    )
