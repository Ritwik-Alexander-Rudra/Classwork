import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')

#Open Close High Low Volume are features (but which ones are meaningful?)
#Useless features are not helpful
#Features are attributes that make up the label - the label is the prediction to the future

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT', 'PCT_change','Adj. Volume']]
#Price will be the label; so far, the only price we even have in df is Adj. Close

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)
#You can't have blank spaces in the data, so you put something that the program can see is
#a clear outlier in the data, and thus ignores it

forecast_out = int(math.ceil(0.01*len(df)))
#Math.ceil takes anything and rounds it up by one.
#The 0.1 uses 10% of the dataframe. If you had 0.01 you would have 1%, etc
#You can predict the future stil, it's just affecting how much data you use

df['label'] = df[forecast_col].shift(-forecast_out)
print(df.head())

X = np.array(df.drop(['label'],1))
#df.drop returns a new dataframe
X = X[:-forecast_out]
X_lately = X[-forecast_out:]
X = preprocessing.scale(X)

#This is #4 learn it better
df.dropna(inplace = True)
Y = np.array(df['label'])
Y = np.array(df['label'])

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, Y_train)

accuracy = clf.score(X_test,Y_test)

forecast_set = clf.predict()

#You 'fit' features and labels




#Typically features are denoted by x and labels are denoted by y



