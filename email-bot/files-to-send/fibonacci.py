def fibonacci(n : int):
    if n == 0 or n == 1:
        return 1
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    
    return fib_list[n - 1]

def main():
    n = int(input())
    print(f"Fibonacci of {n} is: {fibonacci(n)}")

if __name__ == '__main__':
    main()