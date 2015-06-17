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

# ----------------------
# cache_helper_functions
#-----------------------
cache = []
def addToCache(n, c):
    """
    n is an int
    c is cycle length of n
    adds the value and the corresponding cycle length to the cache
    """
    cache.append((n, c))

def isInCache(n):
    """
    n is an int
    returns true if value n is in the cache false otherwise
    """
    inCache = False
    for list in cache:
        if (list[0] == n ):
            inCache = True
            break
        else:
            inCache = False
    return inCache

def getCycleLength(n):
    """
    n is an int
    returns the cycle length of n from the cache 
    """
    cycle = 0
    for list in cache:
        if (list[0] == n ):
            cycle = list[1]
            break
    return cycle


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    #swaps i and j if i > j
    maxLen = 0
    if (i > j) :
        assert i > j
        temp = j
        j = i
        i = temp
    
    #loops through each value withing the range
    while ( i < j + 1) :
        assert i < j + 1
        n = i
        #checks to see if value is in cache
        if (isInCache(n) == True) :
            assert isInCache(n) == True
            cycleLength = getCycleLength(n)
            
            if (maxLen < cycleLength) :
                assert maxLen > 0
                maxLen = cycleLength

        #if value is not in cache, it calculates the cyclelength
        #and adds it to the cache
        else :
            cycleLength = 1
            while (n != 1) :
                assert n > 1
                if (n % 2 == 0) : #if even
                    n = n / 2
                else :
                    n = (3 * n) + 1 #if odd
                cycleLength += 1
                assert cycleLength > 0
            #adds the value and its corresponding cycle length to the cache
            addToCache(i, cycleLength)
            if (maxLen < cycleLength) :
                assert maxLen > 0
                maxLen = cycleLength
        i += 1

    return maxLen
        
                
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
