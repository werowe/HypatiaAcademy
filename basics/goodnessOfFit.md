Assignment: Analyzing Real-World Data and Fitting Distributions
Objective
Use Python to load a dataset, visualize the data, and determine which among the exponential, binomial, or normal distributions best fits the data.
Steps
1. Obtain a Real-World Dataset
Choose a dataset from sources like Kaggle, Data.gov, or Maven Analytics. For simplicity, you can simulate data if real-world data is unavailable.
Example: NYC taxi trip distances or flight delays.
2. Load the Data
Use pandas or numpy to load the dataset into Python.
python
import numpy as np
import pandas as pd

# Simulated data (replace with real-world data)
data = np.random.normal(loc=50, scale=10, size=1000)  # Replace with your dataset
3. Visualize the Data
Plot a histogram of the data to understand its distribution.
python
import matplotlib.pyplot as plt

plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
4. Fit Distributions
Fit exponential, binomial, and normal distributions to the data using scipy.stats.
python
from scipy.stats import expon, binom, norm

# Fit distributions
params_expon = expon.fit(data)
params_binom = (100, np.mean(data)/100)  # Approximation for binomial
params_norm = norm.fit(data)

# Generate PDFs for visualization
x = np.linspace(min(data), max(data), 1000)
pdf_expon = expon.pdf(x, *params_expon)
pdf_binom = binom.pmf(np.round(x), *params_binom)
pdf_norm = norm.pdf(x, *params_norm)
5. Compare Fits
Overlay the fitted distributions on the histogram.
python
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data')
plt.plot(x, pdf_expon, 'r-', label='Exponential Fit')
plt.plot(x, pdf_binom, 'b-', label='Binomial Fit')
plt.plot(x, pdf_norm, 'k-', label='Normal Fit')
plt.legend()
plt.title('Data and Fitted Distributions')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
6. Evaluate Goodness of Fit
Use statistical tests or visual inspection to determine the best fit:
Kolmogorov-Smirnov test (scipy.stats.kstest)
Chi-square goodness-of-fit test
python
from scipy.stats import kstest

# Example: KS test for normal distribution
ks_statistic_norm, p_value_norm = kstest(data, 'norm', args=params_norm)
print(f"KS Statistic (Normal): {ks_statistic_norm}, P-value: {p_value_norm}")
Deliverables
Histogram of the data.
Overlay plot showing fitted distributions.
Summary of goodness-of-fit results for each distribution.
Conclusion on which distribution fits best and why.
This assignment will help you practice:
Loading and visualizing real-world datasets.
Fitting statistical distributions.
Evaluating model fits using both plots and statistical tests.
