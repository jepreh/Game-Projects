"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
Complexity:
Time: O(n)
Space: O(n)
"""


def kidsWithCandies(candies: list, extraCandies: int) -> list:
    maxCandies = max(candies)
    checkTrue = [False] * len(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            checkTrue[i] = True

    return checkTrue


def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    print(kidsWithCandies(candies, extraCandies))
    exit()


if __name__ == "__main__":
    main()