# Q7. A random sample of 10 measurements is taken from a normal population with unknown variance. The
# sample variance is found to be 25. Another random sample of 15 measurements is taken from another
# normal population with unknown variance, and the sample variance is found to be 20. Conduct an F-test
# at the 10% significance level to determine if the variances are significantly different.

from scipy import stats

# Given sample variances and sample sizes
sample_variance_1 = 25
sample_size_1 = 10

sample_variance_2 = 20
sample_size_2 = 15

alpha = 0.10  # 10% significance level

# Degrees of freedom for the two samples
dfn_1 = sample_size_1 - 1
dfn_2 = sample_size_2 - 1

# Calculate the F-statistic
f_statistic = sample_variance_1 / sample_variance_2

# Calculate the critical F-value for the two-tailed test
critical_f_value = stats.f.ppf(1 - alpha / 2, dfn_1, dfn_2)

# Calculate the p-value for the two-tailed test
p_value = 2 * min(stats.f.cdf(f_statistic, dfn_1, dfn_2), 1 - stats.f.cdf(f_statistic, dfn_1, dfn_2))

# Print the results
print("F-Statistic:", f_statistic)
print("Critical F-Value:", critical_f_value)
print("P-Value:", p_value)

# Check the null hypothesis based on the critical F-value and p-value
if f_statistic < critical_f_value:
    print("Fail to reject the null hypothesis: The variances are not significantly different.")
else:
    print("Reject the null hypothesis: The variances are significantly different.")
