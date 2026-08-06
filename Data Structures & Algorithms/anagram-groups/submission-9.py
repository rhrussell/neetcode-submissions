class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - 97] += 1
            
            result[str(freq)].append(word)

        return result.values()