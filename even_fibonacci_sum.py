# This code was assisted by ChatGPT AI in some parts
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def even_fibonacci_sum(limit = 4_000_000):   
    fib1,fib2 = 0, 1
    total = 0
    while fib1 <= limit:
        if fib1 % 2 == 0:
            total += fib1
        fib1, fib2 = fib2, fib1 + fib2
        
    return f"total = {total}"
    
if __name__ == "__main__":
    result = even_fibonacci_sum()
    print(f"Sum of even Fibonacci numbers up to 4 million = {result}")

