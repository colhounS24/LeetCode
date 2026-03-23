from typing import List
# sort the anagram to use as a key in a dict  

# iterate thru the list and if the key matches in the dict O(1), add it to that value in the dict

# return the values in the dicts as a list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value_dict = {}

        for string in strs:
            key = "".join(sorted(string))
            
            if key not in value_dict:
                value_dict[key] = [string]
            else:
                value_dict[key].append(string)
        

        return list(value_dict.values())
            
