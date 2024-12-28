import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
model = LinearRegression()

X = [[1,0],[0,1],[2,0],[1,1]]
y = [0,0,0,1]

model.fit(X,y)
print(model.predict([[2,1]]))