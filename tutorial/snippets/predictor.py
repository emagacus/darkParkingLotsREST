import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.model_selection as ms
import sklearn.preprocessing as pr
from sklearn.linear_model import LinearRegression
from datetime import datetime
from sklearn.preprocessing import PolynomialFeatures
import dateutil.parser
import io
import requests





class Predictor():
    def predict(self,date):

        url="https://raw.githubusercontent.com/emagacus/FlightControl/master/users.csv"
        s=requests.get(url).content
        data=pd.read_csv(io.StringIO(s.decode('utf-8')))
        today = datetime.now()
        
        #print(date)
        date = dateutil.parser.parse(date)
        hours = date.hour
        hours = int(hours) * 100
        if date.minute > 30:
            hours += 100
        else:
            hours += 30

        diffdays = date - today
        #print("hora",hours)

        #data = pd.read_csv('users.csv')
        y = np.asanyarray(data[str(hours)])
        x = np.asanyarray(data['HORA'])

        pred = 0
        inc = 0
        for inp in x:
            #print(inp)
            x[inc] = inc
            #x[inc] = datetime.strptime(inp, '%m/%d/%Y')
            pred = y[inc]
            inc +=1
            

        x = x.reshape((-1, 1))

        #print("DIAS: ", x)
        #print("Hora",y)
        transformer = PolynomialFeatures(degree=2, include_bias=False)
        transformer.fit(x)

        x = transformer.transform(x)

        #print(x)

        model = LinearRegression().fit(x,y)
        r_sq = model.score(x,y)
        #print("RSQ",r_sq)
        #model.fit(y, x)
        #print('coefficient of determination:', r_sq)
        #print('intercept:', model.intercept_)
        #print('coefficients:', model.coef_)
        #print("diferencia de dias",diffdays.days)

        predictDelta = int(model.coef_[0]*(int(diffdays.days)+1))

        pred = pred + predictDelta

        return str(pred)    
        #predictD = np.asanyarray([74])

        #print(model.predict(predictD.reshape(-1,1)))

        """
        poly = pr.PolynomialFeatures(degree=2)
        x = poly.fit_transform(x)
        xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y)
        print(x.shape)
        """