import pandas as pd
def addSMA(df,n):
    df['SMA_'+str(n)]=df.iloc[:,5].rolling(window=n).mean()
    return df