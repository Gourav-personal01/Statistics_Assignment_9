# Q3. Write a Python program that generates random samples from two normal distributions with known
# variances and uses an F-test to determine if the variances are equal. The program should output the F-
# value, degrees of freedom, and p-value for the test.

# Answer - 
import numpy as np
from scipy import stats

# Set the random seed for reproducibility (optional)
np.random.seed(42)

# Generate random samples from two normal distributions
sample_size_1 = 30
sample_size_2 = 30

# Known variances for the two distributions
variance_1 = 4.0
variance_2 = 6.0

# Generate random samples with the specified variances
sample_1 = np.random.normal(loc=0, scale=np.sqrt(variance_1), size=sample_size_1)
sample_2 = np.random.normal(loc=0, scale=np.sqrt(variance_2), size=sample_size_2)

# Perform an F-test to compare the variances
f_statistic = np.var(sample_1, ddof=1) / np.var(sample_2, ddof=1)  # F-statistic
dfn = sample_size_1 - 1  # Degrees of freedom for the numerator
dfd = sample_size_2 - 1  # Degrees of freedom for the denominator
p_value = 2 * min(stats.f.cdf(f_statistic, dfn, dfd), 1 - stats.f.cdf(f_statistic, dfn, dfd))  # Two-tailed p-value

# Output the results
print("F-statistic:", f_statistic)
print("Degrees of Freedom (numerator):", dfn)
print("Degrees of Freedom (denominator):", dfd)
print("Two-tailed p-value:", p_value)

# Check the null hypothesis (equal variances) based on the p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The variances are not equal.")
else:
    print("Fail to reject the null hypothesis: The variances are equal.")
