# Brute Force O(n^2)
# def twoSum( nums: list[int], target: int) -> list[int]:
#     for key1,num1 in enumerate(nums):
#         for key2,num2 in enumerate(nums):
#             if (key1!=key2):
#                 if (num1 + num2) == target:
#                     return [key1,key2] 
## Using Hash Map Time: O(n) Memory:O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        heapMap = {}
        for key,num in enumerate(nums):
            diff = target-num
            if diff in heapMap:
                return [heapMap[diff],key]
            else:
                heapMap[num] = key