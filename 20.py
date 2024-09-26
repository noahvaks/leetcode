# 20. Valid Parentheses

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#my current code is convoluted. I'm going to turn my checking statements into a hash map.

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracketMap = { "(":")",
        "[":"]",
        "{":"}" }

        for i in range(len(s)):
            if s[i] in bracketMap:
                stack.append(s[i])
            if s[i] in bracketMap.values():
                if len(stack) > 0 and s[i] == bracketMap[stack[-1]]: 
                    stack.pop()
                else: return False
        
        return (len(stack) == 0)

'''

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:
#Open brackets must be closed by the same type of brackets.

#a closing bracket with not open bracket is invalid
#check to see if an open bracket has a closing parenthesis


#Open brackets must be closed in the correct order.

#Every close bracket has a corresponding open bracket of the same type.

#i could find the innermost open bracket and determine a corresponding closing bracket, working outwards afterwards. -this would require storing every open bracket for later reference
#essentially i would be ensuring none of the above is broken while keeping a tally- increment by 1 on matching open and decrement by 1 on matching close
#i would have 3 variables that count open parenthesis cases. if it ever goes negative i return false, if it remains positive at the end i return false, i return true at the end!!!

#this doesn't work because what if the case breaks while not negative: ([)(]).. wait.. maybe it does work let me test

#^the above is fine but it does break when open and closed in an incorrect order: ([)]
#i need to ensure that when nested, the innermost are closed first. what if i counted how many layers in i am and then made sure that there was a matching pair before i escape. (([]))

#it's making more sense to make a queue. i will add open parentheses to a list and once i hit a closed parenthesis, match to the last value, remove if valid, and return false if list is empty. i will then return false if the list is not empty at the end. 

#this is a good idea but for some reason i can't get the checker to recognize '[' or '{'
#i think i had a checking return statement in the wrong spot. it works fine

class Solution:
    def isValid(self, s: str) -> bool:
        c = []
        for i in range(len(s)):

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                c += (s[i])
                
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(c) == 0: return False
                if s[i] == ")":
                    if c[-1] != "(": return False
                if s[i] == "]":
                    if c[-1] != "[": return False
                if s[i] == "}":
                    if c[-1] != "{": return False
                del c[-1]
            
        return (len(c) == 0)
'''
