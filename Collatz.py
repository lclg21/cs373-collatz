#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    array = []
    arrayB = []
    if (i <= j):
        assert(i <= j)
        while (i < j+1):
            assert (i < j+1)
            n = i
            cycleLength  = 1
            while ( n != 1 ):
                if (n % 2 == 0): #if even
                    n = n / 2
                else:
                    n = (3 * n) + 1 #if odd

                cycleLength = cycleLength + 1
                assert( cycleLength > 0)
            array.append(cycleLength)
            i = i + 1
            assert(i > 0)

        array.sort()
        arrayLen = len(array)
        maxCycleLength = array[arrayLen - 1]

        return maxCycleLength

    elif i > j:
        assert (i > j)
        while (j < i+1):
            assert(j < i+1)
            n = j
            cycleLength  = 1
            while ( n != 1 ):
                if (n % 2 == 0): #if even
                    n = n / 2
                else:
                    n = (3 * n) + 1 #if odd
                    
                cycleLength = cycleLength + 1
                assert(cycleLength > 0)
            arrayB.append(cycleLength)
            j = j + 1
            assert(j > 0)

        arrayB.sort()
        arrayBLen = len(arrayB)
        maxCycleLength = arrayB[arrayBLen - 1]

        return maxCycleLength
                
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
