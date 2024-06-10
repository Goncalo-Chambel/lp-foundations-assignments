"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample() -> pd.DataFrame:
    """Fixture to load a sample of the eu_life_expectancy.tsv file to serve as 
    input of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv", sep="\t")


@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample_expected() -> pd.DataFrame:
    """Fixture to load the expected output of cleaning the eu_life_expectancy_raw_sample.tsv file"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample_expected.csv")

@pytest.fixture(scope="session")
def actual_countries():
    """Fixture for getting the list of the actual countries"""
    with open(FIXTURES_DIR / "actual_countries.txt", encoding='utf-8') as f:
        countries = [line.strip() for line in f.readlines()]
    return countries
