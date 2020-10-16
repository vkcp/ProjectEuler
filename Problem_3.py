"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


factors = []
number = 600851475143
total = 1

for i in range(2, 600851475143):
    if number % i == 0:
        factors.append(i)
        total = i * total
        if total == 600851475143:
            print(factors)
            break
        number = number // i
        i = 2
