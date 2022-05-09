## solution from https://www.youtube.com/watch?v=B1k_sxOSgv8
from operator import length_hint

from more_itertools import strictly_n
from numpy import result_type


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result 

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, string):
        result, i = [],0

        while i < len(string):
            j = i 
            while string[i] != "#":
                j+=1
            length = int(string[i:j])
            result.append(string[i+1:j+1 + length])
            i = j+1+ length
        return result
            
