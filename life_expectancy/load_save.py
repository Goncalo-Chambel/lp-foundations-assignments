import pandas as pd

def load_data(filename, sep="\t") -> pd.DataFrame:
    """Function to load data from file"""
    data = pd.read_csv(filename, sep=sep)
    return data

def save_data(data: pd.DataFrame) -> None:
    """Function to save data to file"""
    data.to_csv("life_expectancy/data/pt_life_expectancy.csv", index=False)
