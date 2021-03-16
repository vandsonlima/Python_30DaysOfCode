#!/bin/python3

"""
    Objective
        Today, we are building on our knowledge of arrays by adding another dimension. 
        Check out the Tutorial tab for learning materials and an instructional video.
"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxval = None
    for j in range(4):
        for i in range(4):
            add = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
            if maxval ==None:
                maxval=add
            elif add>maxval:
                maxval=add
    print(maxval)