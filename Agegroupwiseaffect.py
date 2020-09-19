import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"Age group percent cases"
"The Plot gives the rough idea about how covid-19  affected different age group people in india in early stages"

d = pd.read_excel('c1dataset/IndiaAgeGroupDetails.xlsx')
palette=sns.color_palette("rocket_r")
sns.barplot(x='AgeGroup',y='TotalCases',data=d,palette=palette).set_title('Cases in different age group in India')
plt.show()