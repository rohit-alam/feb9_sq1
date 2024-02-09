def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    num_terms = 10

    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
