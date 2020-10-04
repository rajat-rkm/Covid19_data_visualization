import webbrowser

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium import plugins
#from IPython.core.display import display, HTML

df1=pd.read_excel("c1dataset/india_all_state.xlsx")
df=pd.read_excel("c1dataset/Indian Coordinates.xlsx")

df_full=pd.merge(df,df1,on='Name of State / UT')
print(df_full)
#print(df_full.columns)

map=folium.Map(location=[20.5937, 78.9629],zoom_start=4.6,tiles="Stamen Terrain")

for lat,long,name,value in zip(df_full['Latitude'],df_full['Longitude'],df_full['Name of State / UT'],df_full['Total_case']):
    folium.CircleMarker([lat,long],radius=value//6500,popup=('<strong>State</strong>:' + str(name).capitalize() + '<br>''<strong>Total Cases</strong>' + str(value) + '<br>'),color='red',fill_color='red',opacity=0.3).add_to(map)

map1=folium.Map(location=[20.5937, 78.9629],zoom_start=4.6,tiles='Stamen Terrain')

for lat,long,name,value in zip(df_full['Latitude'],df_full['Longitude'],df_full['Name of State / UT'],df_full['Recovered']):
    folium.CircleMarker([lat,long],radius=value//4500,popup=('<strong>State</strong>:' + str(name).capitalize() + '<br>''<strong>Recovered Cases</strong>' + str(value) + '<br>'),color='Blue',fill_color='blue',opacity=0.3).add_to(map1)


map2=folium.Map(location=[20.5937, 78.9629],zoom_start=4.6,tiles='Stamen Terrain')

for lat,long,name,value in zip(df_full['Latitude'],df_full['Longitude'],df_full['Name of State / UT'],df_full['Total Deaths']):
    folium.CircleMarker([lat,long],radius=value//250,popup=('<strong>State</strong>:' + str(name).capitalize() + '<br>''<strong>Deaths Cases</strong>' + str(value) + '<br>'),color='#900020',fill_color='#90002',opacity=0.7).add_to(map2)





#to open file automatically
map.save('Maps/India_state_covid_cases.html')
map1.save('Maps/India_state_recovered.html')
map2.save('Maps/India_state_covid_deaths.html')
print("Choose map \n"+"Maps/India_Totalcase.html\n"+"Maps/India_state_recovered.html\n"+"Maps/India_state_covid_deaths.html")
a=input("Enter Map Name/Path ")
output_file = a
new = 2
webbrowser.open(output_file, new=new)



'''
def auto_open(path, f_map=None):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)
'''
