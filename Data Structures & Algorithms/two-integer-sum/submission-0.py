class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map={}# dict to store number->index mapping

        for i in range(len(nums)):
            num=nums[i]#current number
            complement=target-num#number we need 

            if complement in index_map:
                return[index_map[complement],i]
            index_map[num]=i


        return []        


        