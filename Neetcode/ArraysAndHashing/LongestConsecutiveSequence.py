# Given array of integers

# Return the length of the largest consecutive sequence

# nums = [2,20,4,10,3,4,5]. Answer = 4

# Hashmap, where we iterate thru the values, and we only determine the start of the sequence iff n-1 doesn't exist
# Using a hashmap for o(1) lookups

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        longest_seq = 0

        # Building the set
        lookup = set(nums)
        
        
        # For each value in the set
        for num in lookup:
            # Presume it is the start of seq
            if (num - 1) not in lookup:
                seq = 1
                while (num + 1) in lookup:
                    seq += 1
                    num += 1
                longest_seq = max(seq, longest_seq)
            else:
                continue
        return longest_seq

