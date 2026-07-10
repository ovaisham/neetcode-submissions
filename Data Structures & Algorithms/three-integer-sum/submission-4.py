class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            else:
                target = -num
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    if nums[j] + nums[k] == target:
                        ret.append([num, nums[j], nums[k]])
                        j = j + 1
                        while nums[j] == nums[j - 1] and j < k:
                            j = j + 1
                    elif nums[j] + nums[k] < target:
                        j = j + 1
                    else:
                        k = k - 1

        return ret