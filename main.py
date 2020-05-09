import loadPrice
import priceClean
#import pandas as pd
def main():
    df = priceClean.priceClean(loadPrice.loadPrice())
    print(df)
	
if __name__ == "__main__":
    main()