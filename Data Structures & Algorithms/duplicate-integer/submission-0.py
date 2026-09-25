class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={} #creating a dict
        for num in nums:
            if num in freq:
                return True #duplicate found
            freq[num]=1


        return False        


        


        

        