from life_expectancy.load_strategies.strategy_template import LoadDataStrategy
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.region import Region


class LoadTSVStrategy(LoadDataStrategy):
    default_filename: str = "eu_life_expectancy_raw.tsv"
    
    def load_data(self, foldername: str, country: Region, filename: str) -> pd.DataFrame:   
        """Function to load data from tsv file"""

        filename = filename if filename != "" else self.default_filename
        data_raw = pd.read_csv(foldername / filename, sep="\t")

        data = clean_data(data_raw, country)

        return data