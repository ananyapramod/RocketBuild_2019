import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
import plotly.plotly as ply

data=pd.read_csv('C:\\Users\\canara\\Downloads\\crimes.csv', header=0, parse_dates=[0], squeeze=True, index_col=2)
#print(data.columns)
#print(data.shape)
#print(data.head)
from matplotlib import pyplot
#data.plot()

#pyplot.show()
#autocorrelation_plot(data)
#pyplot.show()

#prediction for  location A only
dataset=data.loc[data['Location']=='A']
#print(dataset)
z=dataset.pop('Location')
X=dataset.values

split=int(0.7*len(X))
train=X[0:split]
test=X[split:]

#data = pd.Series(dataset[''], index=frame.time_field)

from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(train, order=(5,1,1))
model_fit = model.fit(disp=0)

output = model_fit.forecast()
ypred = output[0]
per=train[split-1]
if(per>ypred):
    print("Crimes predicted to increase by  "+str((per-pred)/per))
else:
    print("Crimes predicted to decrease by  "+str((ypred-per)/per))
print("Predicted number of crimes for the next month:"+str(ypred[0]))
