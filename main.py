import numpy as np
import pandas as pd
import os

# list_files =[]
# for filename in os.walk('archive'):
#     for i in filename[2]:
#         list_files.append('archive/'+i)

df_results = pd.read_csv('archive/races.csv')
df_circuits = pd.read_csv('archive/circuits.csv')
df_constructor_results = pd.read_csv('archive/constructor_results.csv')
df_lap_times = pd.read_csv('archive/lap_times.csv')
df_races = pd.read_csv ('archive/races.csv')

#combine multiple inputs into a bigger dataframe
df = pd.merge(df_races,df_lap_times)
df = pd.merge(df,df_results)
df = pd.merge(df,df_circuits)
df = pd.merge(df,df_lap_times)
df = pd.merge(df,df_constructor_results)
print(df.head())

