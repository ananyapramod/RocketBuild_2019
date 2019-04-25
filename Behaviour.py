import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.model_selection import train_test_split

def get_analysis():
    features = pd.read_csv('data.csv')
    features.head()
    #features.shape()
    #features.summary()
    features.describe()
    features.dropna(inplace=True)
    
    X=features.iloc[:,:-1].values
    Y=features.iloc[:,-1].values
    X_t,X_test,Y_t,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
    
    rf=RFR(n_estimators=300,random_state=42)
    rf.fit(X_t,Y_t)
    print "Model has been trained"
    itemlist=[]
    pred_val=rf.predict(list(X_test))
    for item in pred_val:
        if item<=0.49:
            itemlist.append(0)
        else:
            itemlist.append(1)
    
    return itemlist
print(get_analysis())
