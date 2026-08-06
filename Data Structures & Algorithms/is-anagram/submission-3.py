class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        if len(s) != len(t):
            return False
        else:
            for char in s:
                s_dict[char] += 1

            for char in t:
                t_dict[char] += 1

            for char in s_dict:
                if s_dict[char] != t_dict[char]:
                    return False

            return True