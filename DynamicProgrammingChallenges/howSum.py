# This dynamic programming function checks whether a target number can be calculated from a number list, if so, it will return an array of numbers 
# The base case of this function depends on the targetSum, if the targetSum < 0, return None. If the targetSum == 0, return an array.
# This is then checked during the recursive call, where if howSum(...) does not return None, save the previous array solution + the current num value to memo.
# Where targetSum is the key for the memo dict.
# The value of each key is the array of number solutions.

def howSum(targetSum, numList, memo = None):
    if memo == None:
        memo = {}
    solutions = []

    if targetSum in memo:
        return memo[targetSum]
    if targetSum < 0: 
        return None
    if targetSum == 0: 
        return solutions

    for num in numList:
        REMAINDER = targetSum - num
        solutionResult = howSum(REMAINDER, numList, memo)
        if solutionResult != None:
            memo[targetSum] = [*solutionResult, num]                    # * is a spread call, which takes the previous array values and adds it into the next
            return memo[targetSum]

    memo[targetSum] = None
    return None

def main():
    print(howSum(7, [2,3]))
    print(howSum(7, [5,3,4,7]))
    print(howSum(7, [2,4]))
    print(howSum(8, [2,3,5]))
    print(howSum(300, [7,14]))                                          # Without dynamic programming this will take a long time to calculate


if __name__ == "__main__":
    main()
    exit()




"""
howSum function time:
m = target sum
n = array length (choices we can take)

Brute Force: (exponential time with n^m)
O(n^m * m) time
O(m) space

Memoised: (no longer exponential as 2 is constant in m^2)
O(n * m^2) time
O(m^2) space

"""