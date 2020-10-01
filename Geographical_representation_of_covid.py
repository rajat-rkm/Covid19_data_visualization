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
print(df_full.columns)

map=folium.Map(location=[20,70],zoom_start=3.75)

for lat,long,name,value in zip(df_full['Latitude'],df_full['Longitude'],df_full['Name of State / UT'],df_full['Total_case']):
    folium.CircleMarker([lat,long],radius=value//6500,popup=('<strong>State</strong>:' + str(name).capitalize() + '<br>''<strong>Total Cases</strong>' + str(value) + '<br>'),color='red',fill_color='red',opacity=0.3).add_to(map)
'''
map1=folium.Map(location=[20,70],zoom_start=3.75,tiles='Stamen Terrain')

for lat,long,name,value in zip(df_full['Latitude'],df_full['Longitude'],df_full['Name of State / UT'],df_full['Total_case']):
    folium.CircleMarker([lat,long],radius=value//6500,popup=('<strong>State</strong>:' + str(name).capitalize() + '<br>''<strong>Total Cases</strong>' + str(value) + '<br>'),color='red',fill_color='red',opacity=0.3).add_to(map1)
map.save('Maps/India_state.html')




'''
#to open file automatically
output_file = 'Maps/India_state.html'
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