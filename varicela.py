# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 01:25:33 2025

@author: Walid
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_2017 = pd.read_excel("egresos-2017.xlsx") # causa_egreso_agrupamiento
df_2018 = pd.read_excel("egresos-2018.xlsx") # causa_egreso_agrupamiento
df_2019 = pd.read_excel("egresos-2019.xlsx") # causa_egreso_agrupamiento

#%%

causa_egreso_agrupamiento2017 = df_2017 ["causa_egreso_agrupamiento"]
causa_egreso_agrupamiento2018 = df_2018 ["causa_egreso_agrupamiento"]
causa_egreso_agrupamiento2019 = df_2019 ["causa_egreso_agrupamiento"]


#%%
##### solo varicela  2017 #####

# Filtro: que contenga "varicela"
filtro_varicela_2017 = df_2017["causa_egreso_agrupamiento"].str.contains("varicela", case=False, na=False)


df_varicela_2017 = df_2017[filtro_varicela_2017]

##### solo varicela 2018 ############

# Filtro: que contenga "varicela"
filtro_varicela_2018 = df_2018["causa_egreso_agrupamiento"].str.contains("varicela", case=False, na=False)


df_varicela_2018 = df_2018[filtro_varicela_2018]


####### solo varicela 2019 ############### 


# Filtro: que contenga "varicela"
filtro_varicela_2019 = df_2019["causa_egreso_agrupamiento"].str.contains("varicela", case=False, na=False)


df_varicela_2019 = df_2019[filtro_varicela_2019]

#################### varicela en un dataframe ################
#%%
df_varicela = pd.concat([df_varicela_2017, df_varicela_2018, df_varicela_2019], axis= 0, ignore_index= True)

# unifico las columnas por los nulls

#df_varicela["municipio_nombre"] = df_varicela["municipio_nombre"].combine_first(df_varicela["municipio_nombre"])


#grupo = df_varicela.groupby(["grupo_edad","tipo_egreso"])["cantidad"].sum().reset_index()
#%%
##### a) casos por edad, diferencia entre sexos ####
casos_edad_sexo = df_varicela.groupby(['grupo_edad', 'sexo'])['cantidad'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.barplot(data=casos_edad_sexo, x='grupo_edad', y='cantidad', hue='sexo')

plt.title('Casos de Varicela por Grupo Etario y Sexo')
plt.xlabel('Grupo Etario')
plt.ylabel('Cantidad de Casos')
plt.xticks(rotation=45)
plt.legend(title='Sexo')
plt.tight_layout()
plt.show()
#%%
####### b) Evolucion anual en el perdio 2017-2019 ############

evolucion_anual = df_varicela.groupby(["anio"])["cantidad"].sum().reset_index()

evolucion_anual["anio"] = evolucion_anual["anio"].astype(int)



plt.figure(figsize=(8,5))
plt.plot(evolucion_anual['anio'], evolucion_anual['cantidad'], marker='o')
plt.title('Evolución Anual de Casos de Varicela (2017-2019)')
plt.xlabel('Año')
plt.ylabel('Cantidad de Casos')
plt.grid(True)
plt.xticks([2017, 2018, 2019])
plt.show()


#%%
####### c) y d) Que regiones sanitarias de la provincia de buenos aires, tiene mas casos de varicela ####### 

mapa_calor = df_varicela.groupby(['anio', 'region_sanitaria'])['cantidad'].sum().reset_index()

plt.figure(figsize=(12,6))

sns.heatmap(
    df_varicela.groupby(['anio', 'region_sanitaria'])['cantidad']
    .sum()
    .unstack()
    .fillna(0),
    annot=True,
    fmt=".0f",
    cmap='YlOrRd'
)

plt.title('Mapa de Calor de Casos de Varicela por Región Sanitaria y Año')
plt.xlabel('Región Sanitaria')
plt.ylabel('Año')
plt.tight_layout()
plt.show()






#%% # e) ¿Cuál es el impacto de la varicela en la mortalidad o en las complicaciones graves?
# Agrupación de 'df_varicela' por tipo de egreso y suma de cantidad
mortalidad2 = df_varicela.groupby(['tipo_egreso'])['cantidad'].sum().reset_index()

#### esto de aca es algunas filas juntas hecho a "mano" porque el datasetes intuitivo y corto, arreglando incosistencia en defuncion y traslado a otro establecimiento######
mortalidad = pd.DataFrame({
    'tipo_egreso': ['Alta definitiva', 'Alta transitoria', 'defuncion', 'otro', 'retiro voluntario', 'Traslado a otro establecimiento'],
    'cantidad': [1151, 6, 5, 6, 6, 26]
})


plt.figure(figsize=(10, 6))
sns.barplot(x='tipo_egreso', y='cantidad', data=mortalidad, palette='viridis')

plt.title('Cantidad de Casos por Tipo de Egreso', fontsize=16)
plt.xlabel('Tipo de Egreso', fontsize=14)
plt.ylabel('Cantidad de Casos', fontsize=14)

plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()
#%%
# f)

import matplotlib.pyplot as plt
import seaborn as sns

promedio_anual = mapa_calor.groupby('anio')['cantidad'].mean().reset_index()


def clasificacionRiesgo(cantidad, promedio):
    if cantidad < promedio:
        return "bajo"
    elif cantidad < 1.5 * promedio:  # Riesgo moderado si es entre promedio y 1.5 veces el promedio
        return "moderado"
    else:
        return "alto"  # Riesgo alto si es más de 1.5 veces el promedio


mapa_calor['riesgo'] = mapa_calor.apply(
    lambda fila: clasificacionRiesgo(fila['cantidad'], promedio_anual.loc[promedio_anual['anio'] == fila['anio'], 'cantidad'].values[0]),
    axis=1
)


regiones_alto_riesgo = mapa_calor[mapa_calor['riesgo'] == 'alto']


regiones_riesgo = regiones_alto_riesgo.groupby('region_sanitaria')['cantidad'].sum().reset_index()


regiones_riesgo = regiones_riesgo.sort_values(by='cantidad', ascending=False)


plt.figure(figsize=(12, 6))
sns.barplot(x='cantidad', y='region_sanitaria', data=regiones_riesgo, palette='coolwarm')


plt.title('Regiones con Mayor Riesgo de Brote de Varicela (Riesgo Alto)', fontsize=16)
plt.xlabel('Cantidad de Casos de Varicela', fontsize=12)
plt.ylabel('Región Sanitaria', fontsize=12)
plt.tight_layout()

plt.show()






