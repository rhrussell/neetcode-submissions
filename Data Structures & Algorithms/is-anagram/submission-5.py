from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict = Counter(s) # automatically gets the frequency of characters
            t_dict = Counter(t)

            for char in s_dict:
                if s_dict[char] != t_dict[char]:
                    return False

            return True