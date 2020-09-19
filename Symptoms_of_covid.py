import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"Symptoms for coronavirus"
s = pd.read_excel('c1dataset/Symptoms.xlsx')
sns.set_theme(style="whitegrid")
print("Symptoms of corona and its percentage are")
print(s)
f,axes=plt.subplots(figsize=(15,8))
ax = sns.barplot(x='Percentage',y='Symptom',data=s,palette="mako",ax=axes)
ax.set(xlabel='Percentages', ylabel='Symptoms', title='Symptoms-percentages of covid')
plt.show()