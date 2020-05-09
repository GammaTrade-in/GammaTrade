import loadPrice
import priceClean
import addSMA
#import pandas as pd
def main():
    df = priceClean.priceClean(loadPrice.loadPrice())
    #n=int(input("Enter Period n for SMA \n"))
    df = addSMA.addSMA(df,5)
    return(df)
	
if __name__ == "__main__":
    main()