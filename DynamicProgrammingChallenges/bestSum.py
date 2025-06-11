"""
The function bestSum() takes in targetSum and an array of numbes as arguments.
The function should return an array containing the shortest combinatiion of numbers that add up to exactly the targetsum.
If there isa tie for the shortest combination, you may return any one of the shortest.
"""

def bestSum(targetSum, numList, memo = None):
    if memo == None:
        memo = {}

    shortestLength = None

    if targetSum in memo:
        return memo[targetSum]
    if targetSum < 0:
        return None
    if targetSum == 0:
        return []
    
    # Check for each num in numList the solution to getting the targetSum. Then check whether the solution is shorter in length than the previous solution.
    # If the current solution is shorter than the last, it is now the shortest solution.
    # Return the shortest solution.
    for num in numList:
        REMAINDER = targetSum - num
        result = bestSum(REMAINDER, numList, memo)
        if result != None:
            solution = [*result, num]
            if (shortestLength == None) or (len(solution) < len(shortestLength)):
                shortestLength = solution
    
    memo[targetSum] = shortestLength        
    return shortestLength


def main():
    print(bestSum(7, [2,3]))
    print(bestSum(7, [5,3,4,7]))
    print(bestSum(7, [2,4]))
    print(bestSum(8, [2,3,5]))
    print(bestSum(6, [5,2,2,3,2,1,4]))
    print(bestSum(300, [7,14]))                                                               # Without dynamic programming this will take a long time to calculate.

    exit()


if __name__ == "__main__":
    main()