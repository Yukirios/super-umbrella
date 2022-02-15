# -*- coding: utf-8 -*-

import seaborn as sns #lets present it smooth, features for plotting
import numpy as np #as a math module 
import pandas as pd #as an addition to math module to adjusting series
import matplotlib.pyplot as plt #plotting 
from scipy.signal import argrelextrema #to define local extrema

#reading formated excel file
df = pd.read_excel('test.xlsx', usecols=[0,1], 
                    names= ['Wavelength(nm)', 'Absorption'])
df.set_index('Wavelength(nm)', inplace=True)

#adding local maxima
n = 18 #checking close up dots, kinda the amount of maxima, manually, see below
df.assign() #create additional column in df, its 3 now
df['max'] = df.iloc[argrelextrema(df.values, np.greater_equal,
                    order=n)[0]]['Absorption'] 
                    #appends indeces of relative extrema found by comparing 
                    #values of the dots nearby(n) to new column, tuple <3

def Maxima():
#summarize maxima data and visualize
  
  for i,row in df.dropna().iterrows():
      
      print(f'Local maximum as well is {row.values[0]} at {i} nm')

  absm = df['Absorption'].max()
  wavem = df['Absorption'].idxmax()
  print(f'\n~The most intense maximum is {absm} at {wavem} nm \n')
  print(df['max'].dropna())
#plotting
  sns.set_theme()
  plt.axvline(x=int(wavem), c='violet', linestyle='dashed') #vertical line of violet to the most intense
  plt.scatter(df.index, df['max'], c='g') #local maxima
  plt.plot(df.index, df['Absorption']) #smooth spectrum line
  plt.legend(["_",'Absorption']) #auto legend
  plt.title(excel_file.name.split(".")[0])
  plt.xlabel('Wavelength(nm)')
  plt.show() #show the plot???? mb useless as sometimes shows itself

Maxima()
