# Day 3 comprises of conditional statements. We are asked to take in input and
# Based on the input determine if we should print "Weird" or "Not Weird"
# Link: https://www.hackerrank.com/challenges/30-conditional-statements/problem

if __name__ == "__main__":
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    elif N >= 2 and N <= 5 and N % 2 == 0:
        print("Not Weird")
    elif N >= 6 and N <= 20 and N % 2 == 0:
        print("Not Weird")
    else:
        print("Not Weird")
