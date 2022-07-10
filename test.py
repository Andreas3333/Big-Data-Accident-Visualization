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
# Read in the Dataset
accidentDataframe = dataframe.read_csv(datasetFileName)
# Store all attriute names
attributeNames = accidentDataframe.columns

## Drop all columns that are not of interest to research question
researchAttributes = [] # attributes of interest
# Directly insert attributes of interest into this list
""" Later we can add code to prompt the user for these attribute names """
researchAttributes.append('Start_Time')
researchAttributes.append('State')
researchAttributes.append('County')

# Get list of all attributes that are not of interst
throwawayAttributes = []
for attribute in attributeNames:
    # Insert attribute in throwaway attribute if it is not a researchAttribute
    if attribute not in researchAttributes:
        throwawayAttributes.append(attribute)
# Drop all attributes that are included in throwawayAttributes
accidentDataframe.drop(columns=throwawayAttributes)

