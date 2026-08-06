class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent = "".join([char for char in s if char.isalnum()]).lower()
        
        j = len(sent) - 1
        for i in range(len(sent)):
            if sent[i] != sent[j]:
                return False
            j -= 1
        return True