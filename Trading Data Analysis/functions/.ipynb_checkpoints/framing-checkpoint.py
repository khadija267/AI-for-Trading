# +
import pandas as pd


def five_minute_framing(df):
    
    framed=df.resample('5T').agg({'Symbol': 'last',
        
                        'Open': 'first', 

                        'High': 'max', 

                       'Low': 'min', 

                        'Last': 'last', 

                         '%Chg': 'sum',

                        'Volume': 'sum'})
    return framed

def fifteen_minute_framing(df):
    
    framed=df.resample('15T').agg({'Symbol': 'last',
        
                        'Open': 'first', 

                        'High': 'max', 

                       'Low': 'min', 

                        'Last': 'last', 

                         '%Chg': 'sum',

                        'Volume': 'sum'})
    return framed

def thirty_minute_framing(df):
    
    framed=df.resample('30T').agg({'Symbol': 'last',
        
                        'Open': 'first', 

                        'High': 'max', 

                       'Low': 'min', 

                        'Last': 'last', 

                         '%Chg': 'sum',

                        'Volume': 'sum'})
    return framed

def day_framing(df):
    
    framed=df.resample('D').agg({'Symbol': 'last',
                       'Open': 'first', 

                        'High': 'max', 

                       'Low': 'min', 

                        'Last': 'last', 

                         '%Chg': 'sum',

                        'Volume': 'sum'})
    return framed

def crypto_day_framing(df):
    
    framed=df.resample('D').agg({
                       'Open': 'first', 

                        'High': 'max', 

                       'Low': 'min', 

                        'Last': 'last', 
                         'Volume': 'sum'

                         })
    return framed
# -


