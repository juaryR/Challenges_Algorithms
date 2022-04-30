# my solutions 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {}
        for key,string in enumerate(strs):
            string_sort = "".join(sorted(string))
            if not string_sort in hashMap:
                hashMap[string_sort] = [key]
            else:
                hashMap[string_sort].append(key)
        result = []
        temp_result = []
        for valeu in list(hashMap.values()):
            for key in valeu:
                temp_result.append(strs[key])
            result.append(temp_result)
            temp_result =[]
        return result 