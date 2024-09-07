# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #create hash map from magazine
        b={}
        for i in range(len(magazine)):
            if magazine[i] in b:
                b[magazine[i]] += 1
            else:
                b.update({magazine[i]: 1})
        #check hash map for ransomNote values
        for i in range(len(ransomNote)):
            if ransomNote[i] in b:
                b[ransomNote[i]] -= 1
                if b[ransomNote[i]] == 0:A
                    del b[ransomNote[i]]
            else: return False

        return True

        
