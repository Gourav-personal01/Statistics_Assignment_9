# Q8. The following data represent the waiting times in minutes at two different restaurants on a Saturday
# night: Restaurant A: 24, 25, 28, 23, 22, 20, 27; Restaurant B: 31, 33, 35, 30, 32, 36. Conduct an F-test at the 5%
# significance level to determine if the variances are significantly different.

# Answer - 
from scipy import stats

# Data for Restaurant A and Restaurant B
data_a = [24, 25, 28, 23, 22, 20, 27]
data_b = [31, 33, 35, 30, 32, 36]

alpha = 0.05  # 5% significance level

# Calculate sample variances and sample sizes
variance_a = sum((x - sum(data_a) / len(data_a))**2 for x in data_a) / (len(data_a) - 1)
variance_b = sum((x - sum(data_b) / len(data_b))**2 for x in data_b) / (len(data_b) - 1)

sample_size_a = len(data_a)
sample_size_b = len(data_b)

# Degrees of freedom for the two samples
dfn_a = sample_size_a - 1
dfn_b = sample_size_b - 1

# Calculate the F-statistic
f_statistic = variance_a / variance_b

# Calculate the critical F-value for the two-tailed test
critical_f_value = stats.f.ppf(1 - alpha / 2, dfn_a, dfn_b)

# Calculate the p-value for the two-tailed test
p_value = 2 * min(stats.f.cdf(f_statistic, dfn_a, dfn_b), 1 - stats.f.cdf(f_statistic, dfn_a, dfn_b))

# Print the results
print("F-Statistic:", f_statistic)
print("Critical F-Value:", critical_f_value)
print("P-Value:", p_value)

# Check the null hypothesis based on the critical F-value and p-value
if f_statistic < critical_f_value:
    print("Fail to reject the null hypothesis: The variances are not significantly different.")
else:
    print("Reject the null hypothesis: The variances are significantly different.")
