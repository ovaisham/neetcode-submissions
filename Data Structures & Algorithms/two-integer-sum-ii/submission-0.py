class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        left_moved = False
        while i < j:
            pos_target = numbers[i] + numbers[j]
            print(pos_target, target)
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif pos_target > target:
                j -= 1
            else:
                i += 1
            