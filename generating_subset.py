

def GenerateSubset (R) :
    if (R > N) :
        # Process the subset
        print("[ "+' '.join ( map (str,subset) ) + " ]")
    else :
        # Generate subset with R
        subset.append(R)
        GenerateSubset (R + 1)

        # Generate subset without R
        subset.pop()
        GenerateSubset (R + 1)

# Generating subsets / combinations using recursion.
R = 1
subset = []

N = 4
print("Subsets for set 1: ")
GenerateSubset (R)

N = 2
print("Subsets for set 2: ")
GenerateSubset (R)