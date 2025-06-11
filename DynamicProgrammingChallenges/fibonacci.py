# This dyanmic programming function solves the fibonacci sum at position n
# The previously solved sum of n is saved in the memo dict, where key = n and value = fib sum of n
# The recursive call is saved to the memo[n] 

def fib(n: int, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

def main():
    num = 100
    print(fib(num))

if __name__ == "__main__":
    main()
    exit()