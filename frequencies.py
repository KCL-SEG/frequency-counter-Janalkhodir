"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
     if str(item) in frequencies:
         frequencies[item] += 1
     else:
      frequencies[item] = 1
    return frequencies
