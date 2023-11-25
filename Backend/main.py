import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
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
df.isnull().sum().sum() #Checking if Null value is present
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
fig.write_image("Graph1.png")
# fig.show()


count_2 = df['Country Name'].value_counts()
fig = px.bar(count_2.head(10), x=count_2.head(10).index, y=count_2.head(10).values,
             title='Top 10 Airport Countries with Most Passengers',
             labels={'x': 'Country', 'y': 'Passenger Count'})
fig.write_image("Graph2.png")
# fig.show()


# #Airport Country and continent wise passenger 
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
# #fig.show()

# #Count vs Age with 4 different graphs
plt.figure(figsize=(18,10))
sns.countplot(data=df,x='Age')
plt.xticks(rotation=90)
plt.savefig("Graph5.png", bbox_inches='tight')
# #plt.show()

# #Plot Box of age by Gender
fig = px.box(df, x='Gender', y='Age', color='Gender',
             title='Box Plot of Age by Gender',
             labels={'Age': 'Passenger Age'})
fig.write_image("Graph6.png")
# # fig.show()

# #Distribution Across Nationality
nationality = pd.DataFrame(df['Nationality'].value_counts()).reset_index()
nationality = nationality.head(20)
nationality.sort_values(by='Nationality', ascending=False, inplace=True)
fig=px.pie(nationality, values='count', names='Nationality', hole=0.5, title='Distribution Accross Nationality')
fig.write_image("Graph7.png")
# # fig.show()

# #Pie Chart of on time cancelled and delayed flights
fl_stat = pd.DataFrame(df['Flight Status'].value_counts()).reset_index()
fig = px.pie(fl_stat, values='count', names='Flight Status', color_discrete_sequence=px.colors.sequential.RdBu)
fig.write_image("Graph8.png")
# # fig.show()

# #Box Plot of Age vs Flight Status
plt.figure(figsize=(12, 6))
sns.boxplot(x='Flight Status', y='Age', data=df, palette='Pastel1')
plt.title('Age vs. Flight Status')
plt.xlabel('Flight Status')
plt.ylabel('Age')
plt.savefig("Graph9.png", bbox_inches='tight')
# # plt.show()

# #Create a line plot for Average Age vs. Flight Status
average_age = df.groupby('Flight Status')['Age'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='Flight Status', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age vs. Flight Status (Line Plot)')
plt.xlabel('Flight Status')
plt.ylabel('Average Age')
plt.savefig("Graph10.png", bbox_inches='tight')
# # plt.show()


# # Create a line plot for the count of flights based on 'Departure Date' and Flight Status
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Count', hue='Flight Status', data=df.groupby(['Departure Date', 'Flight Status']).size().reset_index(name='Count'), palette='Set2')
plt.title('Count of Flights Over Time Based on Flight Status')
plt.xlabel('Departure Date')
plt.ylabel('Count of Flights')
plt.legend(title='Flight Status')
plt.savefig("Graph11.png", bbox_inches='tight')
# #plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='Departure Date', y='Age', data=df, hue='Flight Status', palette='viridis', s=100)
plt.title('Age vs. Departure Date')
plt.xlabel('Departure Date')
plt.ylabel('Age')
plt.legend(title='Flight Status')
plt.savefig("Graph12.png", bbox_inches='tight')
# #plt.show()

# # Create a line plot for Average Age vs. Departure Date
average_age = df.groupby('Departure Date')['Age'].mean().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age Over Time')
plt.xlabel('Departure Date')
plt.ylabel('Average Age')
plt.savefig("Graph13.png", bbox_inches='tight')
# #plt.show()

# #end