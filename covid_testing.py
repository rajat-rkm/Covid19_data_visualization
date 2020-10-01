import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_excel("c1dataset/Statetesting.xlsx")
print(df.tail(10))
palette=sns.cubehelix_palette()

"Overall covid-19 testing till August"
testing=df["Testing"].sum()
print("Overall Testing " ,testing  )

"Total postive case out of overall Testing"
positive_Case=df["Positive"].sum()
print("Positive case",positive_Case)

palette=sns.color_palette("tab20b")
sns.set_theme(style="darkgrid")
f,axes=plt.subplots(figsize=(14,7))
a=sns.barplot(y="States",x="Testing",data=df,ax=axes,palette=palette,edgecolor=".3",ci="sd")
a.set(xlabel='Numbers', ylabel='States', title='Testing of covid-19 in each States')
plt.tight_layout()
#a.set_xticklabels(a.get_xticklabels(), rotation=75, ha="right",fontsize=10)"to set x labels"
plt.show()


f,axes=plt.subplots(2,figsize=(14, 8))
a=sns.lineplot(x="S_no",y="Testing",data=df,ax=axes[0],color="b",marker='D',markeredgecolor='black')
b=sns.lineplot(x="S_no",y="Positive",data=df,ax=axes[1],color='#008000',marker='D',markeredgecolor='black')
plt.tight_layout()
plt.show()