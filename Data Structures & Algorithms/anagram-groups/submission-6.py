class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        
        for word in strs:
            char_map = [0] * 26

            for letter in list(word):
                index = ord(letter) - 97
                char_map[index] += 1

            key = ','.join([str(num) for num in char_map])
            
            if key not in word_map:
                word_map[key] = [word]
            else:
                word_map[key].append(word)

        return word_map.values()
 