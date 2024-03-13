#importing DATA
import pandas as pd
import numpy as np

path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df=pd.read_csv(path)
df.head()

#2 Analyzing data
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline
print(df.dtypes)

#what is the data type of the column "peak-rpm"
data_type=df["peak-rpm"].dtype
print(data_type)
# To find the corelation between variables

#df.corr()

#3 To find the correlation between columns 
my_corr=df[['bore','stroke','compression-ratio','horsepower']].corr()
print(my_corr)

#ploting scatter plot of "engine-size" and "price".

sns.regplot(x="engine-size",y="price",data=df)
plt.ylim(0,)

#printing the correlation between the two data
df[["engine-size","price"]].corr()

#printing the plot for highway-mpg with city-mpg
sns.regplot(x="highway-mpg",y="city-mpg",data=df)
plt.ylim(0,)

df[["highway-mpg","city-mpg"]].corr()

#using box plot to define catagorical varables

# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)
#working with descriptive statical analysis
df.describe()

# when we use decribe it skips the type of objects so we use other method to select objects
df.describe(include=['object'])
# to count values
df['drive-wheels'].value_counts()

# to convert series to dataframes
df['drive-wheels'].value_counts().to_frame()


#Value counts
# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)


#Basics of grouping
df['drive-wheels'].unique()

df_group_one = df[['drive-wheels','body-style','price']]
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1
#grouping the results

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot