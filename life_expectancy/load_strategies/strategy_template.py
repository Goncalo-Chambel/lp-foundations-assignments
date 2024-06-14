from abc import abstractmethod, ABC
import pandas as pd

class LoadDataStrategy(ABC):

    @abstractmethod
    def load_data(self, filename: str, country: str) -> pd.DataFrame:
        pass
