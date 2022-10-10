import numpy as np

T_annual_avg = np.array([2,1],np.loadtxt("annual_csv_average.csv",float))
T_annual = np.array(np.loadtxt("annual_csv.csv",float))


def ddx(xi,f,h):  #f is function, xi is initial point, h is step size                                                                                                      

    return ((f(xi+h) - f(xi-h))/(2*h))

print(T_annual,T_annual_avg)
