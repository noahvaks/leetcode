# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make all lowercase and remove non-alphanumerics
        s = re.sub(r'[\W_]', '', s.lower())
        #loop through length of string comparing reversed w normal
        i=0
        j=len(s)-1
        while i < len(s):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
