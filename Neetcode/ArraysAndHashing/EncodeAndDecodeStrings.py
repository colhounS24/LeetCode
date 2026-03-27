from typing import List

class Solution:
    def __init__(self):
        self.delimiter = "\x1F"
   
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{string}{self.delimiter}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = s.split(self.delimiter)[:-1]
        
        return decoded_string