from enum import Enum, auto

class Region(Enum):
    """Class to handle the different regions"""
    AT = auto()
    BE = auto()
    BG = auto()
    CH = auto()
    CY = auto()
    CZ = auto()
    DK = auto()
    EE = auto()
    EL = auto()
    ES = auto()
    EU27_2020 = auto()
    FI = auto()
    FR = auto()
    HR = auto()
    HU = auto()
    IS = auto()
    IT = auto()
    LI = auto()
    LT = auto()
    LU = auto()
    LV = auto()
    MT = auto()
    NL = auto()
    NO = auto()
    PL = auto()
    PT = auto()
    RO = auto()
    SE = auto()
    SI = auto()
    SK = auto()
    DE = auto()
    DE_TOT = auto()
    AL = auto()
    EA18 = auto()
    EA19 = auto()
    EFTA = auto()
    IE = auto()
    ME = auto()
    MK = auto()
    RS = auto()
    AM = auto()
    AZ = auto()
    GE = auto()
    TR = auto()
    UA = auto()
    BY = auto()
    EEA30_2007 = auto()
    EEA31 = auto()
    EU27_2007 = auto()
    EU28 = auto()
    UK = auto()
    XK = auto()
    FX = auto()
    MD = auto()
    SM = auto()
    RU = auto()

    def __str__(self):
        return self.name

    @classmethod
    def get_actual_countries(cls):
        """Method for getting list of actual countries"""
        non_countries = {"EU27_2020", "DE_TOT", "EA18", "EA19", "EFTA", "EEA30_2007",
                         "EEA31", "EU27_2007", "EU28"}
        return [member.name for name, member in cls.__members__.items()
                if name not in non_countries]
    