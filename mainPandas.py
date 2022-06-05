import pandas as pd
import numpy as np

def mainFunction():

    mainDataFrame = pd.read_csv('Cleaned_Laptop_data.csv')

    # Changing the latest and oldest price data to look more accurate
    mainDataFrame.latest_price = mainDataFrame.apply(lambda x: x.latest_price / 100, axis=1)
    mainDataFrame.old_price = mainDataFrame.apply(lambda x: x.old_price / 100, axis=1)

    #okProcessors = []

    



    print(mainDataFrame.head(100))
        
    






mainFunction()