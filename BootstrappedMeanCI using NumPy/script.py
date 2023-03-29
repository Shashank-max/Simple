import numpy as np

def bootstrap_confidence_interval(X, N=1000, alpha=0.05):
    """
    Compute bootstrapped 95% confidence intervals for the mean of a 1D array X.

    Parameters:
    X : array-like
        Input array.
    N : int, optional
        Number of bootstrap samples. Default is 1000.
    alpha : float, optional
        Significance level (e.g., 0.05 for 95% confidence interval). Default is 0.05.

    Returns:
    tuple
        Lower and upper bounds of the confidence interval.
    """
    bootstrapped_means = []
    n = len(X)
    
    for _ in range(N):
        bootstrap_sample = np.random.choice(X, size=n, replace=True)
        bootstrapped_means.append(np.mean(bootstrap_sample))
    
    bootstrapped_means = np.sort(bootstrapped_means)
    lower_index = int(N * alpha / 2)
    upper_index = int(N * (1 - alpha / 2))
    
    lower_bound = bootstrapped_means[lower_index]
    upper_bound = bootstrapped_means[upper_index]
    
    return lower_bound, upper_bound

# Example usage:
X = np.random.normal(loc=10, scale=2, size=1000)  # Example data (normally distributed with mean 10, std dev 2)
lower, upper = bootstrap_confidence_interval(X)
print("Bootstrapped 95% confidence interval for the mean:", (lower, upper))