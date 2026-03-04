"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Sliding window algo
 
"""

class Solution:
    def characterReplacement(s: str, k: int) -> int:
        # Firstly what is the size of the window at the start
        # If we think about it, we want to pick the letter that we are in at the minute and then keep increasing the window k times, subtracting 
        # from k everytime that we see a different char

        window_size = 1
        max_window = 0
        k_counter = k
        
        for i in range(len(s)):
            j = i
            while k_counter >= 0 and j < len(s)-1:
                if s[j] == s[j+1]:
                    window_size += 1
                    j +=1
                else:
                    window_size += 1
                    k_counter -= 1
                
                if window_size > max_window:
                    max_window = window_size
                window_size = 1

        return max_window


print(Solution.characterReplacement("aaaaa",1 ))    