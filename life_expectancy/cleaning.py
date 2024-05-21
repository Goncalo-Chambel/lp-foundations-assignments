import re
import pandas as pd
from .region import Region

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


def clean_data(data: pd.DataFrame, country:Region) -> pd.DataFrame:
    """Function used to clean raw data"""

    composite_columns = data.columns[0].split(",")
    composite_columns[-1] = composite_columns[-1].split("\\")[0]

    split_columns = data.iloc[:, 0].str.split(",", expand=True)
    split_columns.columns = composite_columns

    df_transformed = pd.concat([split_columns, data.iloc[:, 1:]], axis=1)

    df = pd.melt(df_transformed, id_vars=composite_columns, var_name="year", value_name="value")
    df["year"] = df["year"].astype("int64")
    df["value"] = df["value"].apply(to_float)

    df = df.rename(columns={"geo": "region"})

    df.dropna(inplace=True)

    df = df[df["region"] == country.name]
    return df
