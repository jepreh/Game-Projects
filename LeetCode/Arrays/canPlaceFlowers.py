"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
 return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

# My initial solution
def canPlaceFlowers(flowerbed, n):
    count = 0
    if (flowerbed[0] == 0 and len(flowerbed) == 1 and n == 1) or n == 0:
        return True
    
    for index in range(len(flowerbed)):
        if index == 0 and flowerbed[index] == 0 and flowerbed[index+1] == 0:
            count += 1
            flowerbed[index] = 1
        if index != 0 and index < len(flowerbed) - 1 and flowerbed[index] == 0 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
            count += 1
            flowerbed[index] = 1
        if index == len(flowerbed) - 1 and flowerbed[index] == 0 and flowerbed[index-1] == 0:
            count += 1
            flowerbed[index] = 1
        if count == n:
            return True
    return False

# Optimised solution
def canPlaceFlowersOpt(flowerbed, n):
    count = n
    length = len(flowerbed)
    i = 0

    if n == 0:
        return True

    while i < length:
        if flowerbed[i] == 0:
            prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
            next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            if prev_empty and next_empty:
                flowerbed[i] = 1
                count -= 1
                i += 1
                if count == 0:
                    return True
        i += 1
    return False
 

def main():
    flowerbed = [1,0,1,0,1,0,1]
    n = 0

    # print(canPlaceFlowers(flowerbed, n))
    print(canPlaceFlowersOpt(flowerbed, n))
    exit()


if __name__ == "__main__":
    main()