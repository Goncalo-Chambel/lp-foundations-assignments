import pandas as pd
from . import DATA_DIR, FIXTURES_DIR
from .cleaning import clean_data

if __name__ == "__main__":

    original_data = pd.read_csv(DATA_DIR / "eu_life_expectancy_raw.tsv", sep="\t")
    generated_input = original_data.sample(n=10, random_state=0)
    generated_input.to_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv",
                            index=False, sep="\t")

    generated_output = clean_data(generated_input)
    generated_output.to_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample_expected.csv",
                            index=False)
    