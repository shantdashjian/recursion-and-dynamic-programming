def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# Complexity Analysis:
# O(n ^ 2) time | O(n) space

# Test Cases:
print(fib(1))
print(fib(7))
print(fib(10))
print(fib(50))