class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif sorted(list(s)) != sorted(list(t)):
            return False
        else:
            return True