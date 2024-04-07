import argparse
import re
import pandas as pd


def to_float(value):
    """Helper function to convert values to float"""
    try:
        return float(value)
    except ValueError:
        try:
            found = re.findall(r"[-+]?\d*\.\d+|\d+", value)
            return float(found[0]) if found else None
        except ValueError:
            return None


def load_data() -> pd.DataFrame:
    """Function to load data from file"""
    data = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t")
    return data

def save_data(data: pd.DataFrame) -> None:
    """Function to save data to file"""
    data.to_csv("life_expectancy/data/pt_life_expectancy.csv", index=False)

def clean_data(data: pd.DataFrame, country:str="PT") -> pd.DataFrame:
    """Function used to clean raw data"""

    composite_columns = data.columns[0].split(",")
    composite_columns[-1] = composite_columns[-1].split("\\")[0]

    split_columns = data.iloc[:, 0].str.split(",", expand=True)
    split_columns.columns = composite_columns

    df_transformed = pd.concat([split_columns, data.iloc[:, 1:]], axis=1)

    df = pd.melt(df_transformed, id_vars=composite_columns, var_name="year", value_name="value")
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].apply(to_float)

    df = df.rename(columns={"geo": "region"})

    df.dropna(inplace=True)

    df = df[df["region"] == country]
    return df

if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    args = parser.parse_args()

    data_raw = load_data()
    data_cleaned = clean_data(data_raw, args.country)
    save_data(data_cleaned)
