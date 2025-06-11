# !!! This is the howSum function written by ChatGPT to include print statements at each step !!!
# You’ll see when base cases are hit (targetSum == 0 returns []).
# Each recursive call and return shows the current solutionResult.
# When numbers are combined and stored in memo, you see exactly how the solution is built step-by-step.
# Memo hits to avoid recomputation.
# Try running it and watch how the empty list [] returned at base case becomes the seed for building the full solution as recursion unwinds!

def howSum(targetSum, numList, memo=None):
    if memo is None:
        memo = {}
    solutions = []

    if targetSum in memo:
        print(f"Memo hit for targetSum={targetSum}: {memo[targetSum]}")
        return memo[targetSum]
    if targetSum < 0:
        print(f"targetSum {targetSum} < 0, returning None")
        return None
    if targetSum == 0:
        print(f"Base case hit: targetSum == 0, returning empty list []")
        return solutions  # []

    for num in numList:
        remainder = targetSum - num
        print(f"Trying num={num} for targetSum={targetSum}. Calling howSum({remainder})")
        solutionResult = howSum(remainder, numList, memo)
        print(f"Returned from howSum({remainder}): {solutionResult}")

        if solutionResult is not None:
            combined = [*solutionResult, num]
            memo[targetSum] = combined
            print(f"Setting memo[{targetSum}] = {combined}")
            return combined

    memo[targetSum] = None
    print(f"No combinations found for targetSum={targetSum}. Setting memo[{targetSum}] = None")
    return None


def main():
    print("Result for howSum(7, [2, 3]):")
    print(howSum(7, [2, 3]))
    print("\nResult for howSum(7, [5, 3, 4, 7]):")
    print(howSum(7, [5, 3, 4, 7]))
    print("\nResult for howSum(7, [2, 4]):")
    print(howSum(7, [2, 4]))
    print("\nResult for howSum(8, [2, 3, 5]):")
    print(howSum(8, [2, 3, 5]))
    print("\nResult for howSum(300, [7, 14]): (may take some time without DP)")
    print(howSum(300, [7, 14]))


if __name__ == "__main__":
    main()