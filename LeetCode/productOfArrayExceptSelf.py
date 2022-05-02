## Solutions from https://www.youtube.com/watch?v=bNvIQI2wAjk
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult =[1]*(len(nums))
        
        prefix = 1 
        for i in range(len(nums)):
            mult[i] = prefix
            prefix *= nums[i]
        sufix = 1 
        for i in range(len(nums)-1,-1,-1):
            mult[i] *= sufix
            sufix *= nums[i]
        return mult
        
