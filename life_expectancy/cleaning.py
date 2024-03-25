import argparse
import re
import pandas as pd


def to_float(value):
    try:
        # First, attempt to directly convert to float
        return float(value)
    except ValueError:
        try:
            # If direct conversion fails, try extracting float using regular expression
            found = re.findall(r"[-+]?\d*\.\d+|\d+", value)
            return float(found[0]) if found else None
        except:
            # If all fails, return None or some default value
            return None


def clean_data(country="PT"):
    """Function used to clean raw data"""

    data_raw = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t")
    # Splitting the first composite column into separate columns
    composite_columns = data_raw.columns[0].split(",")
    composite_columns[-1] = composite_columns[-1].split("\\")[
        0
    ]  # Adjusting the last column name to remove '\time'

    split_columns = data_raw.iloc[:, 0].str.split(",", expand=True)
    split_columns.columns = composite_columns

    # Joining the split columns with the original dataframe (minus the composite column)
    df_transformed = pd.concat([split_columns, data_raw.iloc[:, 1:]], axis=1)
    # print(df_transformed["2021"])
    # Unpivoting the data to long format
    df = pd.melt(
        df_transformed, id_vars=composite_columns, var_name="year", value_name="value"
    )
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].apply(to_float)

    df = df.rename(columns={"geo": "region"})

    df.dropna(inplace=True)

    df = df[df["region"] == country]
    df.to_csv("life_expectancy/data/pt_life_expectancy.csv", index=False)


if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    args = parser.parse_args()
    clean_data(args.country)
