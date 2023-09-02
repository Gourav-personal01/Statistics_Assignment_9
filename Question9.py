# Q9. The following data represent the test scores of two groups of students: Group A: 80, 85, 90, 92, 87, 83;
# Group B: 75, 78, 82, 79, 81, 84. Conduct an F-test at the 1% significance level to determine if the variances
# are significantly different.

# Answer - 
from scipy import stats

# Data for Group A and Group B
group_a_scores = [80, 85, 90, 92, 87, 83]
group_b_scores = [75, 78, 82, 79, 81, 84]

alpha = 0.01  # 1% significance level

# Calculate sample variances and sample sizes
variance_a = sum((x - sum(group_a_scores) / len(group_a_scores))**2 for x in group_a_scores) / (len(group_a_scores) - 1)
variance_b = sum((x - sum(group_b_scores) / len(group_b_scores))**2 for x in group_b_scores) / (len(group_b_scores) - 1)

sample_size_a = len(group_a_scores)
sample_size_b = len(group_b_scores)

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
