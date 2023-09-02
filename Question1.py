# Q1. Write a Python function that takes in two arrays of data and calculates the F-value for a variance ratio
# test. The function should return the F-value and the corresponding p-value for the test.

import scipy.stats as stat
import numpy as np

worker1 = [18,19,22,25,27,28,41,45,51,55]
worker2 = [14,15,15,17,18,22,25,25,27,34]

# Calculating f test 

f = np.var(worker1)/np.var(worker2)
print(f)

# Degree of freedom
df1 = len(worker1)-1
df2 = len(worker2)-1 
significance_value = 0.05

critical_value = stat.f.ppf(q =1-significance_value,dfn = df1,dfd=df2)

print(critical_value)

if f > critical_value:
    print("Reject the Null Hypothesis")
else:
    print("We fail to reject the Null Hypothesis")

print(f"f_value is : {f}")
print(f"p_value is : {critical_value}")
