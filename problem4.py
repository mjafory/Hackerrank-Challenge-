# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Output Format

# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output

# 15
# Explanation

# The primary diagonal is:

# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:

#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15


# I tried no-sense code first to get deep idea for solving the problem. Please ignore it

# a_matrix = [
#  [11, 2, 4],
#     [4, 5, 6],
#     [10, 8, -12]
# ]

# add_1 = 0
# add_2 = 0
# add_1_reverse = 0


# for i in range(len(a_matrix)):
#     add_1 += a_matrix[i][i]
#     add_1_reverse = a_matrix[::-1]
#     add_2 += add_1_reverse[i][i]
#     dif = abs(add_1 - add_2)

# print(a_matrix)
# print(add_1_reverse)
# print(add_1)
# print(add_2)
# print(dif)

# def dia_deff(a_matrix):
  
#   add_1 = 0
#   add_2 = 0
#   add_1_reverse = 0
  
  
#   for i in range(len(a_matrix)):
#       add_1 += a_matrix[i][i]
#       add_1_reverse = a_matrix[::-1]
#       add_2 += add_1_reverse[i][i]
#       dif = abs(add_1 - add_2)
#       return dif

# a_matrix = [
#  [11, 2, 4],
#     [4, 5, 6],
#     [10, 8, -12]
# ]


# result = dia_deff(a_matrix)

# print(result)


# this is solution: 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
        add1 = 0
        add2 = 0
        add1_reverse = 0
        
        for i in range(len(arr)):
            add1 += arr[i][i]
            add2 += arr[i][len(arr) - 1 - i]
            
        diff = abs(add1 - add2)
        return diff
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
