# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# import joblib

df = pd.read_csv('cropdataNew3.csv')

# dataset['experience'].fillna(0, inplace=True)

# dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

X = df.iloc[:, :7].values
y = df.iloc[:, -1].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 2021, stratify=y)

#Converting words to integer values
# def convert_to_int(word):
#     word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
#                 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
#     return word_dict[word]

# X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.ensemble import RandomForestClassifier
# regressor = LinearRegression()

#Fitting model with trainig data
from sklearn.metrics import recall_score, accuracy_score, confusion_matrix
rfc = RandomForestClassifier( )
#It is showing error because our dataframe has feature names but we should fit the data as 2d array(or matrix) with values for training or testing the dataset.
#hence X.values instead of X
rfc.fit(X, y)



# Saving model to disk
pickle.dump(rfc, open('model2.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model2.pkl','rb'))
# joblib.dump(rfc, "model.pkl")
print(model.predict([[0.518518519,0.179012346,0.302469136,29.94349168,93.90741192,6.251420275,20.39020503]]))
# print(X)
# print(y)