Part 1 - MultiIndex object by combining the elements of the 'letters' list (['A', 'B', 'C']) with the elements of the 'numbers' list (0 to 9). 
Then, utilize this MultiIndex to index a Series containing random numbers. Name this Series as 'multi'.

Part 2 - Ensure that the index of the MultiIndex is sorted in lexicographical order, as this is a prerequisite for correct functionality when indexing with a MultiIndex.

Part 3 - Swap the levels of the MultiIndex so that it becomes (letters, numbers). 
After doing this, verify if the new Series is correctly lexically sorted. If it isn't, ensure to sort it accordingly.
