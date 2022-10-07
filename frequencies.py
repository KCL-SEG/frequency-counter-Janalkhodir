"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        stringItem = str(item)
        if stringItem in frequencies:
            frequencies[stringItem] += 1
        else:
            frequencies[stringItem] = 1

    return frequencies
