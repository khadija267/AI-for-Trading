# for sticky label
from IPython.display import HTML
# import libraries
import pandas as pd
# set print options to the maximum
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.options.display.max_colwidth=200
# remove scientific float printing
pd.set_option('display.float_format', lambda x: '%.3f' % x)
def sticky(df):

