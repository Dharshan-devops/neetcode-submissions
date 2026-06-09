class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_1 = [ch for ch in s]
        list_2 = [ch for ch in t]
        print(sorted(list_1))
        print(sorted(list_2)) 
        if sorted(list_1) == sorted(list_2):
            return True 
        return False

        