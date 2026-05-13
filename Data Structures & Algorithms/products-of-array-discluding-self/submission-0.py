class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fullProd = 1
        zerosList = []
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zerosList.append(i)
            else:
                fullProd *= nums[i]
        zeroSet = set(zerosList)
        print(zeroSet)
        if len(zeroSet) > 1:
            return [0]*len(nums)
        elif len(zeroSet) == 1:
            for i in range(len(nums)):
                if i not in zeroSet:
                    output.append(0)
                else:
                    output.append(fullProd)
            return output
        else:
            for i in range(len(nums)):
                output.append(int(fullProd / nums[i]))
            return output
            
        
        