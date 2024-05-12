import pandas as pd
from . import DATA_DIR

def load_data(filename, sep="\t") -> pd.DataFrame:
    """Function to load data from file"""
    data = pd.read_csv(filename, sep=sep)
    return data

def save_data(data: pd.DataFrame, filename = DATA_DIR / "pt_life_expectancy.csv") -> None:
    """Function to save data to file"""
    data.to_csv(filename, index=False)
