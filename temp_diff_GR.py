#Code by Grady Robbins
#Worked with Bella Macias

import numpy as np

T_annual_avgstart = np.loadtxt("annual_csv_average.csv",float,skiprows=1) # basic file import
T_annualstart = np.loadtxt("annual_csv.csv",float, skiprows=1)
T_annual_avg = np.reshape(T_annual_avgstart,(2,13)) #converting to preferred form
T_annual = np.reshape(T_annualstart,(2,137))

Time_annual = T_annual[0] #seperating data sets into temps and time
Temp_annual = T_annual[1]
Time_annual_avg = T_annual_avg[0]
Temp_annual_avg = T_annual_avg[1]

def ddx(xi,f,h):  #f is function, xi is initial point, h is step size                                                                                                      

    return ((f(xi+h) - f(xi-h))/(2*h))

#print(T_annual,T_annual_avg)
