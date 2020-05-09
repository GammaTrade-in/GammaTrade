import pandas as pd
def loadPrice():
	df = pd.read_csv (r'C:\Users\singh\Desktop\GammaTrade\RELIANCE.NS.csv')
	print ("Prices Loaded")
	return df