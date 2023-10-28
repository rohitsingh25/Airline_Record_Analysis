import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df=pd.read_csv("Airline Dataset Updated.csv", parse_dates=["Departure Date"])
df.head(11)
df.info()
df.nunique()
df.isnull().sum().sum() 
df['Gender']=df['Gender'].astype('category')
df['Gender'].unique()
df['Age']=df['Age'].astype(int)
_, ax = plt.subplots(figsize=(12, 12), ncols=2, nrows=2,  )
columns = [key for key, value in df.nunique().to_dict().items() if value < 10]
for index, column in enumerate(columns):
    df[column].value_counts().plot(ax=ax.ravel()[index] ,kind='bar', legend=True)
count_1 = df['Gender'].value_counts()
count_1
fig = px.pie(count_1, values=count_1.values, names=count_1.index,title= "Distribution of passengers accross Genders")
fig.show()
count_2 = df['Country Name'].value_counts()
fig = px.bar(count_2.head(10), x=count_2.head(10).index, y=count_2.head(10).values,
             title='Top 10 Airport Countries with Most Passengers',
             labels={'x': 'Country', 'y': 'Passenger Count'})
fig.show()
