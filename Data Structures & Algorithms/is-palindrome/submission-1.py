class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                clean_string += s[i].lower()
        return clean_string == clean_string[::-1]