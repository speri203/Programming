# Day 7 requires you to reverse an array and print out its content.
# Link: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    # Alternatives to reversing an array include
    # 1. reversed(list)
    # 2. list.reverse()
    reversed_arr = arr[::-1]
    for i in reversed_arr:
        print(i, end=" ")
