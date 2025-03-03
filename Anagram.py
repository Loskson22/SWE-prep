class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first false case
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)