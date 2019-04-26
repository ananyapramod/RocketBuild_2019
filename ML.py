from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
from sklearn.metrics import accuracy_score

data=pd.read_csv('C:\\Users\\canara\\Downloads\\crimeML.csv')
#print(data.shape)
#print(data.head)
#print(data.describe)
dataset=data.loc[data['Location']=='A']

dataset.plot()
pyplot.show()
#autocorrelation_plot(data)
z=dataset.pop('Date')
z=dataset.pop('Location')

Y=dataset.pop('Robbery')
X=dataset

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,train_size=0.8)
model=LinearRegression().fit(xtrain,ytrain)
ypred=model.predict(xtest)
print("Predicted number of crimes in Location A :",end="")
print(ypred[0])