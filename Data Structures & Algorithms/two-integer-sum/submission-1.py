class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        remainder = {}
        for index in range(len(nums)):
            remainder[target - nums[index]] = index
        for i in range(len(nums)):
            if nums[i] in remainder:
                if i!= remainder[nums[i]]:
                    return [i, remainder[nums[i]]]
            else:
                continue
