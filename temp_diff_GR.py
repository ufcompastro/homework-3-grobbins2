#Code by Grady Robbins
import matplotlib.pyplot as plt
import numpy as np
#defined functions for reference:
def ddx_central(xi,f,h):  #f is function, xi is initial point, h is step size                                  
    return ((f(xi+h) - f(xi-h))/(2*h))

def ddx_forward(xi,f,h):  #f is function, xi is initial point, h is step size                                                                                             
    return ((f(xi+h) - f(xi))/(h))

def ddx_backwards(xi,f,h):  #f is function, xi is initial point, h is step size                                                                                           
    return ((f(xi+h) - f(xi-h))/(h))

T_annual_avgstart = np.loadtxt("annual_csv_average.csv",float,skiprows=1) # basic file import, aided by Bella Macias in this part only
T_annualstart = np.loadtxt("annual_csv.csv",float, skiprows=1)
Time_annual = list(T_annualstart[:,0]) #seperating variables
Temp_annual = list(T_annualstart[:,1])
Time_annual_avg = list(T_annual_avgstart[:,0])
Temp_annual_avg = list(T_annual_avgstart[:,1])
r =Time_annual_avg.reverse() #reversing all lists so in correct order
r =Temp_annual_avg.reverse()
r =Time_annual.reverse()
r =Temp_annual.reverse()
dT_annual = np.zeros(len(Time_annual),float) #creating empty array to set values in
for n in range(0,len(Time_annual)):
    h = 1
    if n == 0:  #forward derivative at first term: (Temp[1]-Temp[0])/1 h = 1 x0 = 0
        dT_annual[n] = (Temp_annual[n+h]-Temp_annual[n])/h
    if n == len(Time_annual)-1: #backwards derivative at last term: (Temp[Time[len(Time_annual)]]-Temp[Time[len(Time_annual)]-1])/h
        dT_annual[n] = (Temp_annual[n]-Temp_annual[n-h])/h
    if n!=0 and n!= len(Time_annual)-1 : #central derivative for rest
        dT_annual[n] = (Temp_annual[n+h] - Temp_annual[n-h])/(2*h) 
print("the rate of change of Temp per year is",dT_annual)
dT_annual_avg = np.zeros(len(Time_annual_avg),float)
for n in range(0,len(Time_annual_avg)):
    h = 10
    if n == 0:  #repeating for decades                                                                                       
        dT_annual_avg[n] = (Temp_annual_avg[n+1]-Temp_annual_avg[n])/h
    if n == len(Time_annual)-1:                                        
        dT_annual_avg[n] = (Temp_annual_avg[n]-Temp_annual_avg[n-1])/h
    if n!=0 and n!= len(Time_annual_avg)-1 :
        dT_annual_avg[n] = (Temp_annual_avg[n+1] - Temp_annual_avg[n-1])/(2*h)
print("the rate of change of Temp for the 10 year averaging is",dT_annual_avg)
plt.plot(Time_annual, dT_annual)
plt.xlabel('Years')
plt.ylabel('change in Temperature')
plt.savefig('robbins_hw3a.png', dpi=300)
plt.plot(Time_annual_avg, dT_annual_avg)
plt.xlabel('Years')
plt.ylabel('change in Temperature')
plt.savefig('robbins_hw3b.png', dpi=300)
