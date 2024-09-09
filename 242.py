# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #map each character with frequency 
        #go into other array and decrement by frequency
        #check if anything is not 0
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in d:
                return False
            d[t[i]] -= 1
        for i in d.values():
            if i != 0: return False
        return True


            




        
