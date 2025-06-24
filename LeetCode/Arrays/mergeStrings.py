"""
You are given two string word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.
Return the merged string.

The first mergeStrings function is my intial approach with a time complexity of up to O((n+m)^2)
The second solution is the optimised version from perplexity with a time complextity of O(n+m)
My solution is unoptimised as I use string addition instead of appending a list. This is inefficient due to how python handles concatenating strings. 
Each call to add mergeWord to mergeWord, python will create a new string and copy the content over. This results in excess overhead.
"""

# My solution
def mergeStrings(word1:str, word2:str) -> str:
    mergedWord = ''
    length1, length2 = len(word1), len(word2)
    if length1 > length2: 
        for i in range(length2):
            mergedWord = mergedWord + word1[i] + word2[i]
        mergedWord = mergedWord + word1[length2:]
    else:
        for i in range(length1):
            mergedWord = mergedWord + word1[i] + word2[i]
        mergedWord = mergedWord + word2[length1:]  

    return mergedWord

# Perplexity Solution
def mergeStringsOpt(word1: str, word2: str) -> str:
    mergeString = []
    i, j = 0, 0

    # Process the alternating charcters
    while i < len(word1) and j < len(word2):
        mergeString.append(word1[i])
        mergeString.append(word2[j])
        i += 1
        j += 1
    
    # Append remaining characters from either word
    mergeString.append(word1[i:])
    mergeString.append(word2[j:])
    return ''.join(mergeString)

def main():
    word1 = 'abcd'
    word2 = 'pqr'

    print(mergeStrings(word1, word2))
    print(mergeStringsOpt(word1, word2))
    exit()


if __name__ == "__main__":
    main()