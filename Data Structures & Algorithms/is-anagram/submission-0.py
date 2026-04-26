class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pool_s = {}
        pool_t = {}
        for l in s:
            if l in pool_s:
                pool_s[l] +=1
            else:
                pool_s[l] = 1
        for l in t:
            if l in pool_t:
                pool_t[l] +=1
            else:
                pool_t[l] = 1
        return pool_s == pool_t

        