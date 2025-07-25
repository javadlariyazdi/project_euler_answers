# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#Brute_Force  #List_Comprehension
print(sum(i for i in range(1,1000) if i % 5 == 0 or i % 3 == 0 ))

#Mathematical (using arithmetic series formula)
def method2():
    def sum_divisible_by(n):
        p = (999 // n)
        return n * p * (p + 1) // 2
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
    
