import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr
import datetime 


aapl = pdr.get_data_yahoo('AAPL', start="2017-01-01", end="2017-04-30")