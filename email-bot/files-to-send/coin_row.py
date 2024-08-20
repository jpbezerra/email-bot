def coin_row(size : int, coins : list) -> int:
    result = [0 for i in range(size + 2)]
    result[1] = coins[1]

    for i in range(2, size + 2):
        result[i] = max(coins[i] + result[i - 2], result[i - 1])
    
    return result[size + 1]

def main():
    size = int(input())
    coins = [0]

    for i in range(size + 1):
        coins.append(int(input()))

    print(f"The maximum sum is: {coin_row(size, coins)}")

if __name__ == "__main__":
    main()