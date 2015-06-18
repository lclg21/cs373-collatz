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
def isInCache(n):
    cycle = 0
    c = 0
    inCache = False
    for v, c in cache:
        if v == n:
            inCache = True
            cycle = c
            break
    return (inCache, c)

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
        inCacheValue, cache_cycle = isInCache(n)
        #checks to see if value is in cache
        if (inCacheValue == True) :
            assert isInCache(n) == True
            cycleLength = cache_cycle
            
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
                    n = n >> 1    #use right shit for faster performance
                else :
                    n = ((3 * n) + 1) >> 1 #if odd
                cycleLength += 2
                assert cycleLength > 0

            if (i > 99550):
                #adds the value and its corresponding cycle length to the cache
                cache.append((i, cycleLength))
                
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
