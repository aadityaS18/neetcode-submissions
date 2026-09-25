class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):# check the length of the string

            return False

        count={}# create a dict to count chars in s 
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1

        # subtract counts using chars in t

        for char in t:
            if char not in count:
                return False #char not in s 

            count[char]-=1
            if count[char]<0:
                return False

        return True #if all counts are - it is an anagram                          
        