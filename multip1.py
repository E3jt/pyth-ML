import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

all = pd.read_csv("data.csv")
df = pd.DataFrame(all)

print("dane przed skalowaniem:")

print (df)
X = df[['Units Sold', 'Total Profit']]
y = df['Total Cost']

X = X.values

scaledX = scale.fit_transform(X)
print(scaledX)

rege = linear_model.LinearRegression()

rege.fit(scaledX, y)


scaled = scale.transform([[5123, 841183.06]])


predictedogolem = rege.predict([scaled[0]])

print(predictedogolem)
