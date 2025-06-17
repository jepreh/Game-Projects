"""
This algorithm checks whether 2 strings are anagrams of eachother. This has a time complexity of O(n) and a space complexity of O(n)
Both strings are iterated through the same for loop and the count of each character at i is added to the hash map (freqTable)
If both words are anagrams they should have the same count per character and the hash map value mod 2 should result in 0. 
"""

def anagramCheck(word1, word2, n, m):
    checkValid = False
    freqTable = {}

    if n!= m:
        return checkValid
    
    for i in range(n):
        if word1[i] in freqTable:
            freqTable[word1[i]] += 1
        else:
            freqTable[word1[i]] = 1

        if word2[i] in freqTable:
            freqTable[word2[i]] += 1
        else:
            freqTable[word2[i]] = 1

    for key in freqTable:
        if freqTable[key] % 2 != 0:
            return checkValid
    
    checkValid = True
    return checkValid

def main():
    word1 = "AABB"
    word2 = "AABB"
    n = len(word1)
    m = len(word2)
    print(anagramCheck(word1, word2, n, m))

if __name__ == "__main__":
    main()
    exit()