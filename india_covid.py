import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
This Visualization is for dataset between 30 jan 2020 to 6 Aug 2020
'''
df = pd.read_csv("c1dataset/finalcomplete.csv")
df1= pd.read_csv("c1dataset/death_newrecord.csv")
#print(df.head(15))

df.drop(['Latitude','Longitude'],axis=1,inplace=True)
#print(df.columns)

"Total cases in india till 06 august 2020"
total_cases=df['New cases'].sum()
print("Total cases in india till 06 august 2020",total_cases)

"Graphical representation1 "

a=sns.relplot(x="dates",y="New case",kind="line",ci=False,data=df1)
a.fig.autofmt_xdate()
plt.show()
'''
"Total Recovered in india till 06 august 2020"
recovered=df['New recovered'].sum()
print("Total Recovered case in india till 06 august 2020",recovered)
"Graphical representation2 "
b=sns.relplot(x="dates",y="Recovered",kind="line",ci=False,data=df1,palette='g')
b.fig.autofmt_xdate()
plt.show()

"Total Active Case in india till 06 august 2020"
total_Active=df['New cases'].sum() - df['New recovered'].sum() + df['New Death'].sum()
print("Total Active Cases in india till 06 august 2020",total_Active)


"Total Deaths in india till 06 august 2020"
total_deaths=df['New Death'].sum()
print("Total Deaths in india till 06 august 2020",total_deaths)

"Graphical representation3 "
c=sns.relplot(x="dates",y="Deaths",kind="line",ci=False,markers=True,data=df1)
c.fig.autofmt_xdate()
plt.show()

"Comparison between Case,Deaths and Recovered"
f,axes=plt.subplots(3,figsize=(7, 14))
sns.lineplot(x="s_no",y="New case",data=df1,ax=axes[0],palette="Blues")
sns.lineplot(x="s_no",y="Recovered",data=df1,ax=axes[1],palette="Green")
sns.lineplot(x="s_no",y="Deaths",data=df1,ax=axes[2],palette="Reds")

plt.tight_layout()
plt.show()

'''

#*******************************************************************************************************************










