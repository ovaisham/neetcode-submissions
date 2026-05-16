class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join([s[i] for i in range(len(s)) if s[i].isalnum()]).lower()
        s_reverse = "".join([s[-i] for i in range(1, len(s)+1) if s[-i].isalnum()]).lower()
        
        print(s_reverse)
        return s_clean == s_reverse