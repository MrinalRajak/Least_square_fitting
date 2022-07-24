# Least square fit(Straight line)

import math as m
x=[];y=[]
with open("data.txt", "r") as file:
    result=[[float(x) for x in line.split()]for line in file]
    print (result)
    x=[i[0] for i in result]
    y=[i[1] for i in result]
print ("\n",x)
print (y)
# Above code first reads the data from the text file and
# then converts into 2D list then 1D list x and y

f=open("fitting_data.txt", "w")
n=int(input("\nEnter the number of inputs: "))
#x=[0.0007,0.0303,0.0600,0.0903,0.1237,0.1647,0.2148,0.2555,0.3051]
#y=[0.0252,0.3031,0.5894,0.8757,1.204,1.633,2.088,2.475,2.938]
xx=[];xy=[];ssxx=0.;
for i in range(n):
    '''
    x.append(input('x_input'))
    y.append(input('y_input'))
    '''
    xx.append(x[i]*x[i])
    xy.append(x[i]*y[i])

sx=sum(x)
sy=sum(y)
sxx=sum(xx)
sxy=sum(xy)
avg_x=sx/n
avg_y=sy/n

deno=n*sxx-sx*sx
slope=(n*sxy-sx*sy)/deno
intercept=(sy*sxx-sx*sxy)/deno
print("slope= ",slope,"Intercept= ",intercept)
f.write("slpoe=%f\t Intercept=%f" %(slope,intercept))

Residual_sum_of_squares=0
for i in range(n):
    Residual_sum_of_squares= Residual_sum_of_squares+(y[i]-slope*x[i]-intercept)**2
print("Residual_sum_of_squares= ", Residual_sum_of_squares)
f.write("\nResidual_sum_of_squares=%f" %( Residual_sum_of_squares))

Reduced_chi_square= Residual_sum_of_squares/(n-2.) # also called sample variance
print("Reduced_chi_square",Reduced_chi_square)
f.write("\nReduced_chi_square=%f" %(Reduced_chi_square))
RMS_of_residuals=Reduced_chi_square**0.5
print("RMS_of_residuals= ",RMS_of_residuals)
f.write("\nRMS_of_residuals=%f" %(RMS_of_residuals))

# To calculate standard errors in slopeand intercept

for i in range(n):
    ssxx+=(x[i]-avg_x)**2
    del_slope=RMS_of_residuals*ssxx**(-0.5)
    del_intercept=RMS_of_residuals*(1./n+avg_x**2/ssxx)**0.5
print("Standard error in slope= ",del_slope)
f.write("\nstandard error in slope=%f" %(del_slope))

print("Standard error in intercept= ",del_intercept)
f.write("\nstandard error in intercept=%f" %(del_intercept))
f.close()




























































