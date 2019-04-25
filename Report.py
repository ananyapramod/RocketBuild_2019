import numpy as np 
import pandas as pd 
import math

def report_back(km, cur_dis, cur_beat, tot_beat):
    df=pd.read_csv('history_1.csv')
    df.describe()
    df.dropna()
    #print df.columns
    df=df.drop(['Beat number'],axis=1)
    avg_speed=[]
    
    for i in range(len(df)):
        avg_speed.append(df['Distance (km)'][i]/df['Time Taken (minutes)'][i])    
    df['Average Speed']=avg_speed
    
    #print df
    
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LinearRegression as LR
    
    X,Y=df[['Distance (km)']],df[['Time Taken (minutes)']]

    X_t,X_test,Y_t,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
    regressor=LR().fit(X,Y)
    
    #plt.plot(X,Y)
    #plt.scatter(X,Y,color='orange')
        
    print "Expected Time of Completion : ",regressor.predict(km)[0][0],"minutes"
    print cur_dis/float(km) * 100,"% distance already covered \n",cur_beat/float(tot_beat) * 100,"% Beat portions covered"
    print "Estimated Time to complete remaining beat points :",regressor.predict(km-cur_dis)[0][0],"minutes"
        
report_back(14,10,4,6)