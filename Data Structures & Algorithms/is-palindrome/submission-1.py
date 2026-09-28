class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right=0, len(s)-1## we are starting one from left and other from right 

        while left<right:
            if not s[left].isalnum():## isalnum() returns if its alphanumeric or not 
               left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left ].lower()!=s[right].lower(): ## compare lowercase versions 
                return False

            else:
                left+=1
                right-=1 #if they match → move both pointers inward

        return True        # the pointers finish crossing → True    







