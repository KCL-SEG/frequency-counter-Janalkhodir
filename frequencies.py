"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    j = 0
    ctr = 0
    for i in range(len(items)):
        if items[j] == str[items[i]]:
            ctr += 1
    frequencies[items[i]] = ctr
    ctr = 0
    j += 1
    return frequencies
