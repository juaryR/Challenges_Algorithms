## my solution 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        storeString = []
        for string in list(s):
            if string.isalnum():
                storeString.append(string)
        string   = "".join(storeString).lower()     
        if (string  == string[::-1]):
             return True    
        
        return False
        