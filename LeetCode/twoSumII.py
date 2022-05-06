class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        tam = len(numbers)
        left = 0 
        rigth = len(numbers)-1
        while not (rigth  == left) :
            if numbers[left] +  numbers[rigth] > target:
                rigth = rigth-1
            if numbers[left] +  numbers[rigth] < target:
                left = left+1
            if numbers[left] +  numbers[rigth] == target:
                return [left+1,rigth+1]

## better solution from https://www.youtube.com/watch?v=cQ1Oz4ckceM
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l, r = 0, len(numbers) - 1
        
#         while l < r:
#             curSum = numbers[l] + numbers[r]
            
#             if curSum > target:
#                 r -= 1
#             elif curSum < target:
#                 l += 1
#             else:
#                 return [l + 1, r + 1] 
