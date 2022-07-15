import pandas as pd
def minute_framing(m,stock):
    '''
    this function to be used with data frame with these columns in order
    => Time => Symbol => Open => High => Low => Last => Change => %Chg => Volume
    '''
    # here is the data set size after time framing
    Range=int(stock.shape[0]/m)
    # make an empty dataset in the same size of stock dataset at first
    splits=stock[:0]
    # loop through new data set size
    # compress each m rows of the original dataset to one row

    for i in range(Range):
    
        # to set time column to be increasing by m values.
        Time=stock.iloc[i*m+m, 0:1]
    
        # to set the symbol column to last value of each m values
        Symbol=stock.iloc[i*m+(m-1), 1:2]
    
        # to set the open column to first value of each m values
        Open=stock.iloc[i*m, 2:3]
    
        # obtain high column for each m values
        High=stock.iloc[i*m:i*m+m, 3:4]
        # to set the high max value
        High_temp=pd.Series(High.max())
    
        # obtain low column for each m values
        Low=stock.iloc[i*m:i*m+m, 4:5]
        # to set the low min value
        Low_temp=pd.Series(Low.min())
    
        # to set the Last column to last value of each m values
        Last=stock.iloc[i*m+(m-1), 5:6]
    
        # obtain change column for each m values
        Change=stock.iloc[i*m:i*m+m, 6:7]
        # to set the sum of each m values
        Change_temp=pd.Series(Change.sum())
    
        # obtain change percent column for each m values
        Change_percent=stock.iloc[i*m:i*m+m, 7:8]
        # to set the sum of each m values
        Change_percent_temp=pd.Series(Change_percent.sum())
    
        # obtain volume column for each m values
        Volume=stock.iloc[i*m:i*m+m, 8:9]
        # to set the sum of each m values
        Volume_temp=pd.Series(Volume.sum())
    
        # combine all data frames above to splits data set
        c=Time.append(Symbol)
        c_c=c.append(Open)
        c1=c_c.append(High_temp)
        c2=c1.append(Low_temp)
        c3=c2.append(Last)
        c4=c3.append(Change_temp)
        c5=c4.append(Change_percent_temp)
        c6=c5.append(Volume_temp)
        splits=splits.append(c6,ignore_index=True)
    return splits
    
#observe the result and assure correctness
#splits.head()