class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)

        for word in strs:
            char_map = [0] * 26
            for char in word:
                char_map[ord(char) - ord('a')] += 1
            word_map[tuple(char_map)].append(word) # you can use tuples as keys but cant use dictionaries or maps

        return word_map.values()
 