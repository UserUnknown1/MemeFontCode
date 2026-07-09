# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from collections import Counter

t = "rat"
s = "tar"

if len(t) != len(s):
    print("not an Anagram!")
else:
    if Counter(s) == Counter(t):
        print("Anagram!")
    else:
        print("not an Anagram!")
