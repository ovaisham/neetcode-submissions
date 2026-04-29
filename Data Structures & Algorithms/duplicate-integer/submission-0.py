class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        for key in count.keys():
            if count[key] > 1:
                return True
        return False
            