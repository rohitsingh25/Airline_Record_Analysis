import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# #Reading the dataset

df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df.head(11)
df.info()
df.nunique()
df.isnull().sum().sum() #Checking if Null value is present

df['Gender']=df['Gender'].astype('category')
df['Gender'].unique()
df['Age']=df['Age'].astype(int)

# Pie chart of passengers 

count_1 = df['Gender'].value_counts()
count_1
fig = px.pie(count_1, values=count_1.values, names=count_1.index,title= "Distribution of passengers accross Genders")
fig.write_image("Graph1.png")
# fig.show()

# #Bar chart of passengers

count_2 = df['Country Name'].value_counts()
fig = px.bar(count_2.head(10), x=count_2.head(10).index, y=count_2.head(10).values, title='Top 10 Airport Countries with Most Passengers',labels={'x': 'Country', 'y': 'Passenger Count'})
fig.write_image("Graph2.png")
# fig.show()

# pie chart based on continents
# #Airport Country and continent wise passenger 
# to show hierarchial data 

df_c= pd.DataFrame(count_2).reset_index().rename(columns={"index": "value", 0: "count"})
con=df.loc[:,['Country Name','Continents']]
con=con.drop_duplicates()
new_df=pd.merge_ordered(df_c,con, fill_method= 'ffill', on= 'Country Name')

fig = px.sunburst(new_df, path=['Continents', 'Country Name'], values='count',
                  color='count', 
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(new_df['count'], weights=new_df['count']),
                  title= "Airport Country and Continent wise Passengers")
fig.write_image("Graph3.png")
# #fig.show()

# #Histogram of Passenger Age 
fig = px.histogram(df, x='Age', nbins=20, color='Gender',
                   title='Histogram of Passengers Age',
                   labels={'Age': 'Passengers Age'})
fig.write_image("Graph4.png")


# #Count vs Age with 4 different graphs
plt.figure(figsize=(18,10))
sns.countplot(data=df,x='Age')
plt.xticks(rotation=90)
plt.savefig("Graph5.png", bbox_inches='tight')


# #Distribution Across Nationality
nationality = pd.DataFrame(df['Nationality'].value_counts()).reset_index()
nationality = nationality.head(20)
nationality.sort_values(by='Nationality', ascending=False, inplace=True)
fig=px.pie(nationality, values='count', names='Nationality', hole=0.5, title='Distribution Accross Nationality')
fig.write_image("Graph7.png")

# #Pie Chart of on time cancelled and delayed flights
fl_stat = pd.DataFrame(df['Flight Status'].value_counts()).reset_index()
fig = px.pie(fl_stat, values='count', names='Flight Status', color_discrete_sequence=px.colors.sequential.RdBu)
fig.write_image("Graph8.png")


# # Create a line plot for the count of flights based on 'Departure Date' and Flight Status
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Count', hue='Flight Status', data=df.groupby(['Departure Date', 'Flight Status']).size().reset_index(name='Count'), palette='Set2')
plt.title('Flight Status based on Departure Date')
plt.xlabel('Departure Date')
plt.ylabel('Count of Flights')
plt.legend(title='Flight Status')
plt.savefig("Graph11.png", bbox_inches='tight')

# # Create a line plot for Average Age vs. Departure Date
average_age = df.groupby('Departure Date')['Age'].mean().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age Over Time')
plt.xlabel('Departure Date')
plt.ylabel('Average Age')
plt.savefig("Graph13.png", bbox_inches='tight')



# Bar Graph : Passengers of Asian countries

continent = 'Asia'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]

data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
# plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
# plt.legend()
# plt.show()
plt.savefig('bar_asia_pass.png', dpi=300)

# Pie Chart : Passengers of Asian countries

continent = 'Asia'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]

data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
# plt.barh([i for i,j in data], [j for i, j in data])
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
# plt.legend()
# plt.show()
plt.savefig('pie_asia_pass.png', dpi=300)


# Bar Graph : Passengers of North American countries

continent = 'North America'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]

data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
plt.savefig('bar_North_America_pass.png', dpi=300)

# Pie Chart : Passengers of North American  countries

continent = 'North America'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]

data = sorted(data, key=lambda x:x[1])[-10:]
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
plt.savefig('pie_North_America_pass.png', dpi=300)

# Bar Graph : Passengers of European countries

continent = 'Europe'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
plt.savefig('bar_Europe_pass.png', dpi=300)

# Pie Chart : Passengers of European countries

continent = 'Europe'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]

data = sorted(data, key=lambda x:x[1])[-10:]
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
plt.savefig('pie_Europe_pass.png', dpi=300)

# Bar Graph : Passengers of South American countries

continent = 'South America'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
plt.savefig('bar_South_America_pass.png', dpi=300)

# Pie Chart : Passengers of South American countries

continent = 'South America'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])

df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
plt.savefig('pie_South_America_pass.png', dpi=300)

# Bar Graph : Passengers of Oceania countries

continent = 'Oceania'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
plt.savefig('bar_Oceania_pass.png', dpi=300)

# Pie Chart : Passengers of Ocenia countries

continent = 'Oceania'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
plt.savefig('pie_Oceania_pass.png', dpi=300)


# Bar Graph : Passengers of African countries

continent = 'Africa'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.barh([i for i,j in data], [j for i, j in data])
plt.savefig('bar_Africa_pass.png', dpi=300)

# Pie Chart : Passengers of African countries

continent = 'Africa'
df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name']==c]['Passenger ID'])) for c in x]
data = [(i,j) for i,j in zip(x, y)]
data = sorted(data, key=lambda x:x[1])[-10:]
plt.pie([j for i,j in data], labels=[i for i, j in data],autopct='%1.1f%%')
plt.savefig('pie_Africa_pass.png', dpi=300)

df=pd.read_csv("Airline_Dataset.csv", parse_dates=["Departure Date"])
# df.head(11)
# df.info()
# df.nunique()
# df.isnull().sum().sum() #Checking if Null value is present

# df['Gender']=df['Gender'].astype('category')
# df['Gender'].unique()
# df['Age']=df['Age'].astype(int)
# _, ax = plt.subplots(figsize=(12, 12), ncols=2, nrows=2,  )
# columns = [key for key, value in df.nunique().to_dict().items() if value < 10]

# for index, column in enumerate(columns):
#     df[column].value_counts().plot(ax=ax.ravel()[index] ,kind='bar', legend=True)


# #Histogram of Passenger Age 
fig = px.histogram(df, x='Age', nbins=20, color='Gender',
                   title='Histogram of Passengers Age',
                   labels={'Age': 'Passengers Age'})
fig.write_image("Graph4.png")



#plt.show()

# # Create a line plot for the count of flights based on 'Departure Date' and Flight Status
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Count', hue='Flight Status', data=df.groupby(['Departure Date', 'Flight Status']).size().reset_index(name='Count'), palette='Set2')
plt.title('Count of Flights Over Time Based on Flight Status')
plt.xlabel('Departure Date')
plt.ylabel('Count of Flights')
plt.legend(title='Flight Status')
plt.savefig("Graph11.png", bbox_inches='tight')
plt.show()


# Create a line plot for Average Age vs. Departure Date
average_age = df.groupby('Departure Date')['Age'].mean().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age Over Time')
plt.xlabel('Departure Date')
plt.ylabel('Average Age')
plt.savefig("Graph13.png", bbox_inches='tight')
plt.show()

#end
