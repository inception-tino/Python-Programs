"""
 program that takes value n from the user: 
 n=5
 1*2*3*4*5 = 120
"""

n = int(input("Enter an integer value for n: "))
prod = 1

for i in range(1, n + 1):
    prod *= i

print(f"The product of all integers from 1 to {n} is: {prod}")






