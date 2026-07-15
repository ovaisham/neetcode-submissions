class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        l_i = 0
        m_i = (len(nums) - 1)//2
        r_i = len(nums)
        while m_i > 0:
            if nums[l_i] > nums[m_i]:
                nums = nums[l_i:m_i + 1]
            else:
                nums = nums[m_i:r_i]    
            l_i = 0
            m_i = (len(nums) - 1)//2
            r_i = len(nums)
        
        if nums[r_i - 1] < nums[0]:
            min = nums[r_i - 1]
        
        return min

