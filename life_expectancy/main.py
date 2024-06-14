import argparse
from life_expectancy.region import Region
from life_expectancy.load_strategies.strategy_template import LoadDataStrategy 
from life_expectancy.load_strategies.load_tsv import LoadTSVStrategy
from life_expectancy.load_strategies.load_json import LoadJSONStrategy
from .save import save_data
from . import DATA_DIR

def main(arguments: argparse.Namespace) -> None:
    """Function to test the main module"""

    country = arguments.country
    filename = arguments.filename
    load_strategy_str = arguments.load_strategy

    available_classes = {
        "LoadTSVStrategy": LoadTSVStrategy,
        "LoadJSONStrategy": LoadJSONStrategy,
    }
    try:
        selected_class = available_classes[load_strategy_str]
    except KeyError:
        print(f"Strategy class '{load_strategy_str}' not found")
        return
    
    load_strategy: LoadDataStrategy = selected_class()
    data = load_strategy.load_data(DATA_DIR, country, filename)
    save_data(data)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=lambda s: Region[s], choices=list(Region),
                        required=True, help="Filter by this country", default=Region.PT)

    parser.add_argument("--filename", type=str, help="Name of the file containing the data",
                        default="")

    parser.add_argument("--load_strategy", type=str, help="The class used to load the data",
                        default="LoadTSVStrategy")

    args = parser.parse_args()
    main(args)
