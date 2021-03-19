# Day 6 requires you to take in input from the STDIN and then print out
# all of the characters in the even index as a word and all the characters
# in the odd index as a word, Ex: water = wtr ae
# Link: https://www.hackerrank.com/challenges/30-review-loop/problem

for i in range(int(input())):
    s = input().strip()
    print(s[::2] + " " + s[1::2])
