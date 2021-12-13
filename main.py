import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Plan
# Put together results, constructorStandings, driverStandings
# labels = results[positionOrder]
# results - drop: resultID, position, positionText, # points
# constructorStandings - drop: constructorStandingsID, positionText
# driverStandings - drop: driverStandingsID, constructorID, positionText


df_results = pd.read_csv('archive/results.csv')
df_constructor_standings = pd.read_csv('archive/constructor_standings.csv')
df_driver_standings = pd.read_csv('archive/driver_standings.csv')


# clean dataframes
# df_results = df_results.drop(['positionText', 'positionOrder', 'points'], axis=1)  #drop them later because we need to have them at first for accuracy reasons
df_driver_standings.drop('positionText', axis=1)

df_constructor_standings.drop('positionText', axis=1)

# combine same length dataframes
# print(df_results.columns)
# print(df_constructor_standings.columns)
# df_contructor_standing does not have a 'driverId' column
df_merged =pd.merge(df_results,df_constructor_standings, on = ['constructorId','raceId']) # merge the dataframes
results = (df_merged['position_x']).replace("\\N",20)
#df['B'] = np.where(df['B'].between(8,11), 0, df['B'])
results_cat = results
results_cat = results_cat.astype(int)

results_cat = np.where(results_cat.between(4,10),1,results_cat) #anything webtween 4-10 will be given the number 1 category
results_cat = np.where(results_cat<4,0,results_cat) #anything less than one will have 0
results_cat = np.where(results_cat>10,2,results_cat) #above 10 will have the label 2
results_cat = pd.DataFrame(results_cat)
print(results_cat)

df_no_results = df_merged.drop(['resultId', 'constructorStandingsId', 'positionText_x', 'positionText_y','positionOrder', 'points_x','points_y', 'position_x','position_y'], axis=1) #drop all the columns that are verry predictive (the labels)
print(df_no_results.columns)
