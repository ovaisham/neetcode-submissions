class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freqList = []
        output = []
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for key in freqMap.keys():
            freqList.append((freqMap[key], key))
        for topK in sorted(freqList, reverse = True)[:k]:
            output.append(topK[-1])
        return output
        