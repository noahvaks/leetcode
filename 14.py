#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = True #checker
        j = 0 #iterator
        a = "" #return
        s = "" #comparison
        while j < len(min(strs)) and m == True:
            s = strs[0][j] #set comparison to jth char of first string
            for i in strs: #check if all jth chars match match
                if i[j] != s: #break out if don't match
                    m = False 
            if m == True: a+=s
            j+=1
        return a

            

        
