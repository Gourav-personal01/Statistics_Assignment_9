# Q5. A manufacturer claims that the variance of the diameter of a certain product is 0.005. A sample of 25
# products is taken, and the sample variance is found to be 0.006. Conduct an F-test at the 1% significance
# level to determine if the claim is justified.

from scipy import stats

# Given data
claimed_variance = 0.005
sample_variance = 0.006
sample_size = 25
alpha = 0.01  # 1% significance level

# Degrees of freedom for the numerator and denominator
dfn = sample_size - 1
dfd = sample_size - 1

# Calculate the F-statistic
f_statistic = sample_variance / claimed_variance

# Calculate the critical F-value for the two-tailed test
critical_f_value = stats.f.ppf(1 - alpha / 2, dfn, dfd)

# Calculate the p-value for the two-tailed test
p_value = 2 * min(stats.f.cdf(f_statistic, dfn, dfd), 1 - stats.f.cdf(f_statistic, dfn, dfd))

# Print the results
print("F-Statistic:", f_statistic)
print("Critical F-Value:", critical_f_value)
print("P-Value:", p_value)

# Check the null hypothesis based on the critical F-value and p-value
if f_statistic < critical_f_value:
    print("Fail to reject the null hypothesis: The claim is justified.")
else:
    print("Reject the null hypothesis: The claim is not justified.")
