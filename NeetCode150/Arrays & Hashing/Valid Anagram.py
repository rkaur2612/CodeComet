class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        for c in s: #O(n)
            if c not in dict_s: #O(1)
                dict_s[c] = 1 #O(1)
            else:
                dict_s[c] += 1
        
        for c in t: #O(n)
            if c not in dict_s:#O(1)
                return False
            else:
                dict_s[c] -= 1
        
        for k in dict_s:
            if dict_s[k] != 0:
                return False
        return True

        #Space - O(n)
        #Time - O(n)
