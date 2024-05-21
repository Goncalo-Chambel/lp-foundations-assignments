import argparse
from . import DATA_DIR
from .load_save import load_data, save_data
from .cleaning import clean_data
from .region import Region

def main(country):
    """Function to test the main module"""
    data_raw = load_data(DATA_DIR / "eu_life_expectancy_raw.tsv")
    data_cleaned = clean_data(data_raw, country)
    save_data(data_cleaned)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=lambda s: Region[s], choices=list(Region),
                        required=True, help="Filter by this country")
    args = parser.parse_args()
    region = args.country
    main(region)
