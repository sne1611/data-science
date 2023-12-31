# -*- coding: utf-8 -*-
"""Lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFi0mJ1goESZWU-i3g-xoz13he__eImS
"""

import pandas as pd
# from pandas import read_csv
import numpy
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('price.csv')
# df = read_csv('price.csv')
pd.t

df

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')

new_df = df.drop('price',axis='columns')
new_df

price = df.price
price

reg = linear_model.LinearRegression()
reg.fit(new_df,price)

reg.predict([[3200]])

reg.coef_

reg.intercept_

reg.predict([[5000]])

area_df = pd.read_csv("areas.csv")
area_df.head(3)

p = reg.predict(area_df)
p

area_df['prices']=p
area_df

area_df.to_csv("prediction.csv")