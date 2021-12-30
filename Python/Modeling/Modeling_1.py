import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr


def space(n):
    print("\n"*n)

######################################################################################################################################
# A    
y_y=[1,0,1,2,5,1,4,6,2,3,5,4,6,8,4,5,7,9,7,6]    # mmHg blood
x_x=[60,63,65,70,70,70,80,90,80,80,85,89,90,90,90,90,94,100,100,100]  #noise dB



plt.scatter(y=y_y, x=x_x) #scatter plot
plt.title("y vs x")
plt.xlabel("dB")
plt.ylabel("mmHG")
plt.show()

############################################################################################################################################3
#B
print("B\n")
correlation, garbs = pearsonr(x_x, y_y) #garbs==p_vlaue
print("The correlation factors is :"+str(correlation))
space(10)
############################################################################################################################################

#C and D
x_x_np=np.array(x_x)
m, b = np.polyfit(x_x, y_y, 1)  # gradient
plt.plot(x_x, m*x_x_np + b)   #eq
plt.scatter(y=y_y, x=x_x)
plt.title("Line best fit")
plt.xlabel("dB")
plt.ylabel("mmHG")
plt.show()


#########################################################################################################################################################

#E
print("E\n")
formula=m*90 +b
print("There will be about " +str(round(formula,4))+ " mmHg increase in blood pressure at 90dB")
space(10)

###########################################################################################################################################################

#F
print("F\n")

garbage_collector=[]
above5_val=[]
for idx, val in enumerate(x_x):
    form=m*val+b
    if form > 5: 
        garbage_collector.append(form)    #just to check
        above5_val.append(val)    #The value of x which raise y more than 5
ave=np.array(above5_val).mean()   #average of the values
print("For the rise of 5mmHg, the range of the noise is between 85 to 100 dB; the esitmated value is " + str(ave)+ " dB")
