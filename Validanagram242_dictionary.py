# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

t = "rat"
s = "tarzan"

countT = {}
countS = {}
if len(t) != len(s):
    print("Not an Anagram")
else:
    for i in range(len(t)):
        countT[t[i]] = 1 + countT.get(t[i], 0)
        countS[s[i]] = 1 + countS.get(s[i], 0)
    if countT == countS:
        print("We have an anagaram")
