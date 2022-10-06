"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
       frequencies[items[i]] = items.count(items[i])
    return frequencies
