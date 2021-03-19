# Day 10 deals with binary numbers. The goal of this assignment is to convert
# a decimal (base 10) number into its binary representation, then print out
# the length of the longest sequence of 1's in the binary representation.
# Example 13 = 1101 and output should be 2 since longest sequence of 1's is 2.
# Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
if __name__ == "__main__":
    n = int(input())
    output = ""
    while n > 0:
        remainder = n % 2
        n = n // 2
        output += str(remainder)

    print(max(map(len, output.split("0"))))
