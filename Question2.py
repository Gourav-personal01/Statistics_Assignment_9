# Q2. Given a significance level of 0.05 and the degrees of freedom for the numerator and denominator of an
# F-distribution, write a Python function that returns the critical F-value for a two-tailed test.
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