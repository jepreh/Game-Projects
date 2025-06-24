"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

def gcdOfStrings(word1: str, word2:str) -> str:
    # Check the base case:
    if word1 + word2 != word2 + word1:
        return ''
    
    # Assign length variable to each string respectively
    length1, length2 = len(word1), len(word2)
    while length2:
        # Euclid's algorithm to calculate the GCD, using string lengths as n and m
        length1, length2 = length2, length1 % length2
    
    # Return the string up till the GCD
    return word1[:length1]


def main():
    word1 = 'ABCABC'
    word2 = 'ABC'
    print(gcdOfStrings(word1, word2))
    print(gcdOfStrings('ABABABABAB', 'ABAB'))
    print(gcdOfStrings('LEET', 'CODE'))
    exit()


if __name__ == "__main__":
    main()