import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
import os

# use of pandas
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
# Distribution of passengers accross Genders
# fig = px.pie(count_1, values=count_1.values, names=count_1.index,title= "Distribution of passengers accross Genders")
# fig.show()
labels = count_1.index
values = count_1.values
plt.figure(figsize=(8, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of passengers across Genders')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('../Frontend/img/pie_chart.png')
plt.show()
exit(0)


# count_2 = df['Country Name'].value_counts()
# fig = px.bar(count_2.head(10), x=count_2.head(10).index, y=count_2.head(10).values,
#              title='Top 10 Airport Countries with Most Passengers',
#              labels={'x': 'Country', 'y': 'Passenger Count'})
# fig.show()



# df_c= pd.DataFrame(count_2).reset_index().rename(columns={"index": "value", 0: "count"})
# con=df.loc[:,['Country Name','Continents']]
# con=con.drop_duplicates()
# new_df=pd.merge_ordered(df_c,con, fill_method= 'ffill', on= 'Country Name')
# fig = px.sunburst(new_df, path=['Continents', 'Country Name'], values='count',
#                   color='count', 
#                   color_continuous_scale='RdBu',
#                   color_continuous_midpoint=np.average(new_df['count'], weights=new_df['count']),
#                   title= "Airport Country and Continent wise Passengers")
# fig.show()
# fig = px.histogram(df, x='Age', nbins=20, color='Gender',
#                    title='Histogram of Passengers Age',
#                    labels={'Age': 'Passengers Age'})
# fig.show()
# plt.figure(figsize=(18,10))
# sns.countplot(data=df,x='Age')
# plt.xticks(rotation=90)
# plt.show()
# fig = px.box(df, x='Gender', y='Age', color='Gender',
#              title='Box Plot of Age by Gender',
#              labels={'Age': 'Passenger Age'})
# fig.show()
# nationality = pd.DataFrame(df['Nationality'].value_counts()).reset_index()
# nationality = nationality.head(20)
# nationality.sort_values(by='Nationality', ascending=False, inplace=True)
# fig=px.pie(nationality, values='count', names='Nationality', hole=0.5, title='Distribution Accross Nationality')
# fig.show()
# fl_stat = pd.DataFrame(df['Flight Status'].value_counts()).reset_index()
# fig = px.pie(fl_stat, values='count', names='Flight Status', color_discrete_sequence=px.colors.sequential.RdBu)
# fig.show()