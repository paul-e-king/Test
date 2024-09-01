"""
Aliquot number explorations
 -- Paul King
 Inspired by Numberphile's "276" video

 Attempts to explore the aliquot sequence: amicable (or sociable) numbers, friendly numbers,
 untouchable numbers, deficient numbers, abundant numbers, and perfect numbers.

 Sociable (amicable) numbers at some point will cycle through the same set of 2, 4 or more numbers forever. No one has
 ever found a cycle of 3 members.

 An "aliquot sum" of N is defined as the sum of the proper factors of N.

 Deficient numbers N have an aliquot sum less than N; abundant numbers N have an aliquot sum greater than N. Perfect
 numbers N have an aliquot sum exactly equal to N.

 The only untouchable number we know about is 5. It is never the sum of any aliquot sequence. 5 itself decays to 1
 right away, so its aliquot sum is just 1.

 Aliquots depend on "proper factors". The proper factors of N do not include N itself.

 Aliquot process: Expands a number's proper factors, adds them, and their sum is an aliquot number.
 Aliquot sequence: Takes the result of the aliquot process, and applies the same process to it as well.

 When an aliquot sequence decays to 1, the sequence terminates.
 Prime numbers all have a single proper factor of 1 and no other proper factors.
 The number 1 itself has no proper factors.

 Sequences which cannot terminate are perfect numbers, whose proper factors add to the same number forever.
 Another interminable sequence would be a number whose factors add to a perfect number, such as 25.

 The first 5 perfect numbers are: 6; 28; 496; 8,128; 33,550,336 (OEIS.org). These get ridiculously huge very quickly.
 There is no way to handle these right now, so you will get an infinite loop.
"""

import math

def faclist(N):
    """
    Function extracts the proper factors of N and returns the list
    :param N: (int) : input parameter for the number to factorize
    :return: Function returns an array (list) of proper factors of N

    max (int) : highest number to search for factors
    i (int) : a counter
    j (int) : holds the second factor where i * j = N
    """
    max = math.floor(math.sqrt(N))
    for i in range(1, max+1):
        if (N % i == 0):
            facs.append(i)
            if (N // i != N): # avoid division by 1
                j = N // i
                if i != j: # avoid perfect squares
                    facs.append(j)
    return facs

def sum(L):
    """
    Add up a list of numbers.
    :param L: An array of integer
    :return: The sum of the values in the array (integer)

    x (int) : extracts an integer from array L
    total (int) : the total of values in the array
    """
    total = 0
    for x in L:
        total = total + x

    return total

"""
Main code
Focusing on numbers <= 1000
(reference: https://mathlair.allfunandgames.ca/aliquotchains2.php)
All prime numbers have a sequence length of 1.
Interesting input values: 8, 24, 102, 138, 150, 180, (276), 312, 528, (552), (564), 570, 600, (660), 720, 726, 
                          840, 858, 870, 936, 960, (966), (996)
The number 702 is said to get too large to calculate, but does end at 1.
Numbers to avoid: all perfect numbers - perfect numbers are not handled yet
Other numbers not handled: cyclic sequences
The numbers 276, 552, 564, 660, 966, 996 have no known maximum number. They have even foiled supercomputers.
"""
import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

R = int(input("Please input a starting number: "))
first = True # first time?
S = 0
count = 0
max = 0
ypoints = []
special = {276,552,564,660,966,996} # a set of special numbers we need to manage more carefully
while S > 1 or first:
    facs = [] # empty list
    if S == 0:
        S = sum(faclist(R))
        first = False
    else:
        S = sum(faclist(S))

    print("{:21,d} ".format(S), end="") # attempt to make nice columns
    if max < S:
        max = S
    count += 1
    if (count % 8 == 0):
        print()
    # ypoints.append(S)
    ypoints.append(math.log10(S))
    if (R in special) and count >= 81: # handle all special cases - just go to 81 terms
        break

print("\nThere were {} terms. Maximum was: {:16,d}".format(count, max))
xp = np.array(range(1, count+1))
yp = np.array(ypoints)
plt.plot(xp, yp)
plt.show()
sys.stdout.flush()