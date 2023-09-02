# Q6. Write a Python function that takes in the degrees of freedom for the numerator and denominator of an
# F-distribution and calculates the mean and variance of the distribution. The function should return the
# mean and variance as a tuple.

def f_distribution_mean_variance(dfn, dfd):
    """
    Calculate the mean and variance of an F-distribution.

    Args:
        dfn (int): Degrees of freedom for the numerator.
        dfd (int): Degrees of freedom for the denominator.

    Returns:
        tuple: Mean and variance of the F-distribution as (mean, variance).
    """
    if dfd <= 2:
        raise ValueError("Degrees of freedom for the denominator (dfd) must be greater than 2.")
    
    mean = dfd / (dfd - 2)
    
    if dfd <= 4:
        raise ValueError("Degrees of freedom for the denominator (dfd) must be greater than 4 for variance calculation.")
    
    variance = (2 * (dfd ** 2) * (dfn + dfd - 2)) / (dfn * (dfd - 2) ** 2 * (dfd - 4))
    
    return mean, variance

# Example usage:
dfn = 3  # Degrees of freedom for the numerator
dfd = 10  # Degrees of freedom for the denominator

mean, variance = f_distribution_mean_variance(dfn, dfd)
print("Mean:", mean)
print("Variance:", variance)
