import pandas as pd
import numpy as np

# Given lists
letters = ['A', 'B', 'C']
numbers = list(range(10))

# Create MultiIndex from the product of the two lists
multi_index = pd.MultiIndex.from_product([numbers, letters], names=['Letter', 'Number'])

# Create a Series of random numbers indexed by the MultiIndex
random_data = np.random.rand(len(multi_index))
multi = pd.Series(random-data, index=multi_index)

print(multi)
