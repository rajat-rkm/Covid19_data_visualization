import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
This Visualization is for dataset between 30 jan 2020 to 6 Aug 2020
'''
df = pd.read_csv("c1dataset/finalcomplete.csv")
df1= pd.read_excel("c1dataset/death_newrecord.xlsx")
#print(df.head(15))

df.drop(['Latitude','Longitude'],axis=1,inplace=True)
#print(df.columns)

"Total cases in india till 06 august 2020"
total_cases=df['New cases'].sum()
print("Total cases in india till 06 august 2020",total_cases)

"Plotting  Total cases"
palette=sns.set_palette("Blues_d",8,0.75)
a=sns.relplot(x="dates",y="New case",kind="line",ci=False,data=df1, marker='s', markeredgecolor='black',palette=palette,height=4,aspect=2)
a.fig.autofmt_xdate()
a.fig.suptitle('Cases in india till 06 august 2020')
plt.show()

"Total Recovered in india till 06 august 2020"
recovered=df['New recovered'].sum()
print("Total Recovered case in india till 06 august 2020",recovered)

"Plotting Total Recovered"
palette1=sns.set_palette("Greens_d",8,0.75)
b=sns.relplot(x="dates",y="Recovered",kind="line",ci=False,data=df1,marker='s', markeredgecolor='black',palette=palette1,height=4,aspect=2)
b.fig.autofmt_xdate()
b.fig.suptitle('Recovered cases in india till 06 august 2020')
plt.show()

"Total Active Case in india till 06 august 2020"
total_Active=df['New cases'].sum() - df['New recovered'].sum() + df['New Death'].sum()
print("Total Active Cases in india till 06 august 2020",total_Active)


"Total Deaths in india till 06 august 2020"
total_deaths=df['New Death'].sum()
print("Total Deaths in india till 06 august 2020",total_deaths)

"Plotting Total Deaths "
palette1=sns.set_palette("Reds_d")
c=sns.relplot(x="dates",y="Deaths",kind="line",ci=False,marker='s', markeredgecolor='black',data=df1,palette=palette1,height=4,aspect=2)
c.fig.autofmt_xdate()
c.fig.suptitle('Deaths in india till 06 august 2020')
plt.show()

"Comparison between Case,Deaths and Recovered"
f,axes=plt.subplots(3,figsize=(7, 14))
sns.lineplot(x="dates",y="New case",data=df1,ax=axes[0],color="b",marker='D',markeredgecolor='black')
sns.lineplot(x="dates",y="Recovered",data=df1,ax=axes[1],color='#008000',marker='D',markeredgecolor='black')
sns.lineplot(x="dates",y="Deaths",data=df1,ax=axes[2],color="r",marker='D',markeredgecolor='black')
plt.tight_layout()
plt.show()


#************************************************Rate of covid *********************************************************
"Recovery Rate in india"
df1 = df1[:-1]
df1['recovery rate'] = df1['Recovered']/df1['New case']*100
sns.lineplot(x='dates', y='recovery rate', data=df1, color='#008000', marker='D', markeredgecolor='black').set_title('Recovery Rate in India')
plt.show()

"Death Rate in india"
q = sns.set_palette("Reds_d")
df1['death rate'] = df1['Deaths']/df1['New case']*100
sns.lineplot(x='dates', y='death rate', data=df1,palette=q, marker='D', markeredgecolor='black').set_title('Death Rate in India')
plt.show()

"The Plots give the idea ,how  with the incearse in covid case the death,Recovery is affected "
sns.set_theme(style='white')
p=sns.set_palette("flare_d")
sns.lineplot(x="New case",y="Deaths",marker='D',markeredgecolor='black',data=df1,palette=p).set_title('Newly infected v/s newly deaths')
plt.show()
p=sns.set_palette("crest_d")
sns.lineplot(x="New case",y="Recovered",marker='D',markeredgecolor='black',data=df1,palette=p).set_title('Newly infected v/s newly recovered')
plt.show()



#*******************************************************************************************************************
#Piechart to Compare Percentage of DEATH vs RECOVERED vs CASE
piedf=pd.DataFrame({"Overall":["Death","Recovered","Overall_Case","Active_case"],
                    "Value":[40593,1328164,1964273,676702]})
color=["#B80F0A","#008000","#87CEEB","#ED9121"]
Explode=(0,0,0,0.1)
overall=piedf["Overall"]
value=piedf["Value"]
plt.pie(value,labels=overall,explode=Explode,colors=color,shadow=True,autopct='%1.1f%%',startangle=60)
plt.title("Covid-19 Affects on India")
plt.show()

