import pandas as pd
from sklearn import linear_model
import numpy as np


def removeNanFromAge (X):
    ageNanCount = X['Age'].isnull().sum()
    
    ageMean = df['Age'].mean()
    
    ageStd = df['Age'].std()

    randomTab = np.random.randint(ageMean - ageStd, ageMean + ageStd, size=ageNanCount)

    X.loc[X['Age'].isnull(), 'Age'] = randomTab

    return X
    
    
    
df = pd.read_csv('data.csv')



def transformSexFromCategoricalToNumerical():

    sex_female_male = pd.get_dummies(df[['Sex']], dtype=int)
    X = pd.concat([df[['Pclass','Age']], sex_female_male], axis=1)

    return X


keys = df.keys()

X = transformSexFromCategoricalToNumerical()
    
X = removeNanFromAge(X)


y = df['Fare']



regr = linear_model.LinearRegression()
regr.fit(X.values, y)

predicted = regr.predict([[2, 25, 0, 1]])
#Mężczyzna 25 lat bilet drugiej klasy
print (predicted)
