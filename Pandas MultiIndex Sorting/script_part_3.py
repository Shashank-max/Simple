# Exchange the levels of the MultiIndex
multi = multi.swaplevel()

# Check if the index of multi is lexicographically sorted
is_sorted = multi.index.is_lexsorted()

if not is_sorted:
    # Sort the index
    multi = multi.sort_index()

print("Is index lexicographically sorted?", multi.index.is_lexsorted())