#import statements
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline


#assign path to variable
path = "/Users/Aaron/OneDrive/Documents/Hackathons/Allstate_Datahack_06-04-17"

#set to working directory
os.chdir(path)

#check for files in dir
list(x in os.listdir('.') for x in ['trainingData.csv', 'testingData.csv'])

#read the file
train = pd.read_csv('trainingData.csv')

#execute head method on train data
train.head()

#plot a histogram of rodents
train.rodents.plot.hist()
plt.title('Histogram of rodents')

#select burglar column and return description
#passes back range of features eg. data type, min max, mean. 
train.burglary.describe()

#read test file
test = pd.read_csv('testingData.csv')

#execute head method on test data
test.head()

#plot density of garbage
train.garbage.plot.density()
plt.title('Density of garbage')

#return dimensions of the array (shape method)
train.shape

#return dimensions of the array (shape method)
test.shape

#Determine which column is contained in the training set and not in the testing set
is_column_missing = list(column not in test.columns for column in train.columns)
train.columns[is_column_missing]

#generate random uniform numbers and use them for predictions
numberOfObservationsInTestSet = len(test.index)
arrayOfPredictions = np.random.rand(numberOfObservationsInTestSet)

#calculate percentile quarters 
np.percentile(arrayOfPredictions, [0, 25, 50, 75, 100])

#creates data frame containing relevant columns
outputDataSet = pd.DataFrame({'inspectionId': test.inspectionId,
                              'response': arrayOfPredictions
                             })

#inspect data before export
outputDataSet.head()

#output comma separated file to current working directory 
outputDataSet.to_csv('submissionExample.csv', index = False)

