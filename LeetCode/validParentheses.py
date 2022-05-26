## solution from https://www.youtube.com/watch?v=WTzjTskDFMg

class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')':'(','}':'{',']':'['}
        stack = [] 
        for val in s:
            if val in hashMap:
                if stack and stack[-1] == hashMap[val]:
                    stack.pop()  
                else:
                    return False
            else:
                stack.append(val)
        
        return True  if not stack else False 