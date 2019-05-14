def fibonacci(n):
    if n == 0: # Base Case 1
        return 0
    if n == 1: # Base Case 2
        return 1
    
    # Recursive case
    return fibonacci(n-2) + fibonacci(n-1)
