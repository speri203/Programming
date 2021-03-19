# Day 11 dealt with 2D arrays. The objective was to find the maximum sum of all hourglasses
# that can be formed within the array.
# Pink : https://www.hackerrank.com/challenges/30-2d-arrays/problem

if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -9 * 6
    for i in range(1, 5):
        for j in range(1, 5):
            hourglass_sum = arr[i - 1][j - 1]
            hourglass_sum = arr[i - 1][j]
            hourglass_sum = arr[i - 1][j + 1]
            hourglass_sum = arr[i + 1][j - 1]
            hourglass_sum = arr[i + 1][j]
            hourglass_sum = arr[i + 1][j + 1]
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    print(hourglass_sum)
