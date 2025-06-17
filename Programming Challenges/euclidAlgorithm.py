def euclidGcd(m: int, n: int) -> int:
    # Base case
    if n == 0:
        return m
    else:
        return euclidGcd(n, m % n)

def euclidLcd(m: int, n: int) -> int:
    # Base case
    return abs(m * n) // euclidGcd(m, n)

def main():
    m = 24
    n = 60
    print(euclidGcd(m, n))
    print(euclidLcd(m, n))

if __name__ == "__main__":
    main()
    exit()