# This dynamic programming function checks whether number in a list can sum to the target number.
# This function returns true if there are numbers in the list that can sum to the target number.

def canSum(targetNumber, numList, memo=None):
    if memo is None:
        memo = {}

    if targetNumber in memo:
        return memo[targetNumber]
    if targetNumber == 0:
        return True
    if targetNumber < 0:
        return False
    
    for num in numList:
        if canSum(targetNumber - num, numList, memo) == True:
            memo[targetNumber] = True
            return True

    memo[targetNumber] = False
    return False


def main():
    print(canSum(7, [2,3]))
    print(canSum(7, [5,3,4,7]))
    print(canSum(7, [2,4]))
    print(canSum(8, [2,3,5]))
    print(canSum(300, [7,14]))


if __name__ == "__main__":
    main()
    exit()