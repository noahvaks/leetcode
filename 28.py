#28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            j=0
            while j < len(needle) and haystack[i+j] == needle[j]: 
                j+=1
                if j == len(needle): return i  
        return -1
