class Solution:
    def containsDuplicate(self, num):
        if len(num) !=  len(set(num)):
            return True
        else: return False   