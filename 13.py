# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        i=0
        for i in range(len(s)):
            if s[i] == 'M': 
                if s[i-1] == 'C' and i>0: sum+=800
                else: sum+=1000
            if s[i] == 'D': 
                if s[i-1] == 'C' and i>0: sum+=300
                else: sum+=500
            if s[i] == 'C': 
                if s[i-1] == 'X' and i>0: sum+=80
                else: sum+=100
            if s[i] == 'L': 
                if s[i-1] == 'X' and i>0: sum+=30
                else: sum+=50
            if s[i] == 'X': 
                if s[i-1] == 'I' and i>0: sum+=8
                else: sum+=10
            if s[i] == 'V':
                if s[i-1] == 'I' and i>0: sum+=3
                else: sum+=5
            if s[i] == 'I': sum+=1
            print(sum)
        return sum
