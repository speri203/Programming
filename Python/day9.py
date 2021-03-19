# Day 9 concerns recursion and the task is to write the factorial alg using recursion
# Should be noted that the answer will not be accepted without recursion.
# Link: https://www.hackerrank.com/challenges/30-recursion/problem?h_r=next-challenge&h_v=legacy
def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n - 1)
