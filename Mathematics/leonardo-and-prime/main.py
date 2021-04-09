#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    
    # Implement an abridged version of the Sieve of Sundaram.
    # The original sieve of Sundaram (1934) finds all prime
    # numbers up to a specified number n. For all integers i,
    # j, such that 1 <= i <= j, i + j + 2ij <= n, then
    # all i + j + 2ij are composite, and the rest prime.
    com = set()
    
    c = 0
    k = (n - 2) // 2
    for i in range(1, k + 1):
        j = i
        g = i + j + 2 * i * j
        while g <= n:
            c += 1
    
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
