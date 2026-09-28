class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n=len(height)
        l=0
        r=n-1 # STARTIG BOTH the pointers 
        max_area=0# initilise max area found so 

        while l<r:# keep checking untile both the pointer meets 
            w=r-l# width is distance btw two pointers
            h=min(height[l],height[r])
            a=w*h# calculates the area

            max_area=max(max_area,a)# Update the maximum area if this one is larger

            if height[l]<height[r]:  # Move the pointer with the shorter height
        # because keeping the shorter side cannot improve the area
                l+=1

            else:
                r-=1

        return max_area            

