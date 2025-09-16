
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def main():
    print("Welcome to gitgud.py!")
    try:
        n = int(input("Enter a positive integer for Fibonacci calculation: "))
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()