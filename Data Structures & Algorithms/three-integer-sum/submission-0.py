class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()# sorted the array 

        for i,a in enumerate(nums):# fix the first number of the triplet 
            if i> 0and a== nums[i-1]:# skips the duplicate values for the first number 
                continue

            l,r=i+1,len(nums)-1# defining the two pointers 

            while l<r:
                threeSum=a+nums[l]+nums[r]# sum of three number 
                if threeSum >0:# sum is large right move ot left 
                    r-=1

                elif threeSum <0:# sum is small move left pointer right 

                    l+=1

                else:
                    res.append([a,nums[l],nums[r]])          
                    l+=1
                    while nums[l]== nums[l-1] and l<r:# skip duplicate values on the left 
                        l+=1
        return res              


        