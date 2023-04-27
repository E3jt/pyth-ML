import pandas as pd
from sklearn import linear_model

all = pd.read_csv("data.csv")


allKeys = all.keys()

df = pd.DataFrame(all)
print(df)

X = df[['Units Sold', 'Total Profit']]
y = df['Total Cost']

regr = linear_model.LinearRegression()
regr.fit(X.values, y)
predictedogolem = regr.predict([[5123, 841183.06]])

print(predictedogolem)
