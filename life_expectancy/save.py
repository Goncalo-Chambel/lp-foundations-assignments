import pandas as pd
from . import DATA_DIR

def save_data(data: pd.DataFrame, filename = DATA_DIR / "pt_life_expectancy.csv") -> None:
    """Function to save data to file"""
    data.to_csv(filename, index=False)
