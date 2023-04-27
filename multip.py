import pandas as pd
from sklearn import linear_model

all = pd.read_csv("data.csv")


allKeys = all.keys()

df = pd.DataFrame(all)
print(df)

X = df[['Ship Date', 'Total Profit']]
y = df['Total profit']

regr = linear_model.LinearRegression()
regr.fit(x.values, y)
predictedogolem = regr.predict([[3/27/2013, 841183.06]])

print(predictedogolem)
