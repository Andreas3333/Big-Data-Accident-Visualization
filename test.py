import csv 
import pandas # Needed for chunking data
import numpy as np # Needed for number processing
import time
from dask import dataframe 

datasetFileName = "US_Accidents_Dec21_updated.csv"

attributes = [] # names of attributes in dataset
records = [] # list of records in dataset

# dataframe = pandas.read_csv(datasetFileName)
# # print the first 20 records
# row1 = dataframe.sample(1)
# print(row1)

accidentDataframe = dataframe.read_csv(datasetFileName)


# # Read the original dataset from csv file
# with open(datasetFileName, "r") as datasetFile:
#     # create csv reader object
#     accidentDataset = csv.reader(datasetFile)

#     # Extact the attribute names from file
#     attributes = next(accidentDataset)

#     # Extract first ten records
#     recordIndex = 0
#     for record in accidentDataset[:10]:
#         records.append(record)
