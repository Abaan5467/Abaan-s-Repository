import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as p


x = np.array([[1],[2],[3],[5]])
y = np.array([6,7,8,10])


x_test = np.array([[4],[7],[10],[80]])

model = LinearRegression()
model.fit(x,y)
prediction = model.predict(x_test)
print(prediction)








