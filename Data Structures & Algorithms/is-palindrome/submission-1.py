class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s_strip = "".join(s.split())
        j = len(s_strip) - 1
        isPalindrome = True
        while i <= j:
            if not s_strip[i].isalnum():
                i += 1
                print(i)
            elif not s_strip[j].isalnum():
                j -= 1
                print(j)
            else:
                if s_strip[i].lower() == s_strip[j].lower():
                    i += 1
                    j -= 1
                    print(i, j)
                else:
                    return False
           
        return isPalindrome    