class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        lh_pointer = 0
        
        st = re.sub(r'[^a-zA-Z0-9]',"",s.lower())
        rh_pointer = len(st) -1

        if len(st) == 1:
            return True
        
        elif len(st) == 2:
            if st[0] == st[1]:
                return True
            else:
                return False

        if len(st) %2 == 0:
            while lh_pointer < rh_pointer:
                if st[lh_pointer] == st[rh_pointer]:
                    lh_pointer += 1
                    rh_pointer -= 1
                    
                else:
                    return False
        else:
            while lh_pointer < rh_pointer -1:
                if st[lh_pointer] == st[rh_pointer]:
                    lh_pointer += 1
                    rh_pointer -= 1
                    
                else:
                    return False
        return True
