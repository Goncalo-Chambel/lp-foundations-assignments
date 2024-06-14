from life_expectancy.load_strategies.strategy_template  import LoadDataStrategy
import pandas as pd
from life_expectancy.region import Region
from typing import Optional

class LoadJSONStrategy(LoadDataStrategy):
    
    default_filename = "eurostat_life_expect.json"
    
    def load_data(self,
                  foldername: str,
                  country: Region,
                  filename: str
                  ) -> pd.DataFrame:
        pass