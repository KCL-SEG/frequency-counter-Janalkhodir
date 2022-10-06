"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        ctr = 0
        for j in range(i):
            if items[i] == str(items[j]):
                ctr += 1
                frequencies[items[i]] = ctr
    return frequencies
