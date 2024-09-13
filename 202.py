# 202. Happy Number

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# -separate the number into digits, square them, and add that

# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# keep track of what numbers we have in a hashmap, if it is 1 or if the number exists, stop

# Those numbers for which this process ends in 1 are happy.
# return isHappy

class Solution:
    def isHappy(self, n: int) -> bool:

        d={} #to store previous values
        d[n] = 0
        # while n not in d:   # loop until happy or not happy
        while d[n] < 2:
            z=0
            n = [int(d) for d in str(n)] #convert to string, then iterate and turn each entry into an int
            for i in n: z += i**2 #square and sum each digit
            n=z
            if n not in d: #increment on reoccurence
                d[n] = 0
            d[n]+=1

        return(n==1)

        
