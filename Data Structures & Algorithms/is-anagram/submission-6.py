class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        s_dict = [0] * 26
        t_dict = [0] * 26

        for letter in s:
            s_dict[ord(letter) - 97] += 1

        for letter in t:
            t_dict[ord(letter) - 97] += 1

        if s_dict == t_dict:
            result = True
        
        return result