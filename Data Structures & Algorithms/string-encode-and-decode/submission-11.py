class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for word in strs:
            result += str(len(word)) + "#" + word
            # adding words like this 4#word
  
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # incrementing until you find the delimiter position
            length = int(s[i:j]) # once found you get the length of the string
            result.append(s[j + 1 : j + 1 + length]) # appending the string from one off the delimiter to the final character in the string
            i = j + 1 + length # set i to the end of the string previous string
  
        return result