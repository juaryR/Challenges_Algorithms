## my solution but have a time Limit because have O(n²)
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#        ## Brute Force O(n2)
#         maxArea = 0 
#         for l in range(len(height) -1 ):
#             for r in range(l+1,len(height)):
#                 area = min(height[l],height[r])* (r-l)  
#                 maxArea = max(maxArea,area)
#         return maxArea
# better solution from https://www.youtube.com/watch?v=UuiTKBwPgAo
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l,r = 0, len(height)-1
        while r > l:
            area = min(height[l],height[r])* (r-l)
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
            maxArea = max(maxArea,area)
        return maxArea