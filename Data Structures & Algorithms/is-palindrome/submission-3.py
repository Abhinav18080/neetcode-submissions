class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(char for char in s if char.isalnum()).lower()
        return result == result[::-1]