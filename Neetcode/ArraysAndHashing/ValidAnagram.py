"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for letter in s[:]:
            if letter in dict_s:
                dict_s.update({letter: dict_s[letter]+1})
            else:
                dict_s[letter] = 1
        
        for letter in t[:]:
            if letter in dict_t:
                dict_t.update({letter: dict_t[letter]+1})
            else:
                dict_t[letter] = 1
        
        if dict_s == dict_t:
            return True
        else:
            return False
