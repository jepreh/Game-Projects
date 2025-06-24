def twoSum(nums = [11,15,7,2], target = 26):
    solution = {}
    for i, num in enumerate(nums):
        REMAINDER = target - nums[i]
        print(REMAINDER)
        if REMAINDER in solution:
            return [solution[REMAINDER], i]
        solution[num] = i
    return None


"""
Complexity
Time: O()
"""

def main():

    print(twoSum())

if __name__ == "__main__":
    main()