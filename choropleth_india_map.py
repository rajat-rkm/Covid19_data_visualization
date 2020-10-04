import json
import webbrowser

import pandas as pd
import folium
india_states=json.load(open("states_india.geojson",'r'))

print(india_states['features'][0])
"necessary things to map geojson with csv file geojson file must have some key so for this"
state_map_id = {}
for feature in india_states['features']:
    feature['id'] = feature['properties']['state_code']
    state_map_id[feature['properties']['st_nm']] = feature['id']
print(state_map_id)

df= pd.read_excel("cherocsv/Indian coordinates.xlsx")
df1=pd.read_excel("cherocsv/india_all_state.xlsx")
df_full=pd.merge(df,df1,on='Name of State / UT')
df_full['state_code']=df_full['Name of State / UT'].apply(lambda x: state_map_id[x])
print(df_full)

map=folium.Map(location=[20.5937, 78.9629],zoom_start=4.6)
fig=folium.Choropleth(geo_data=india_states,name='choropleth',data=df_full,columns=['state_code','Total_case'],key_on='feature.properties.state_code',
                      threshold_scale= [1000,100000,300000,500000,1000000,1500000],
                  fill_color='YlOrRd',
                  fill_opacity=0.7,
                  line_opacity=0.2,
                   legend_name = 'Corona Cases in India till August').add_to(map)


for i in range(0,len(df_full)):
    folium.Marker([ df_full.iloc[i]['Latitude'],df_full.iloc[i]['Longitude']],
                  popup=(  str(df_full.iloc[i]['Name of State / UT']) + '<br>''<strong>Active Cases</strong>:'+ str(df_full.iloc[i]['Active Case']) + '<br>' '<strong>Deaths</strong>:' +str(df_full.iloc[i]['Total Deaths']))
                  ).add_to(map)
map.save('Maps/choroplethIndia_state.html')
output_file = 'Maps/choroplethIndia_state.html'
new = 2
webbrowser.open(output_file, new=new)


#print(df_full.head(8))