class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longestSeqLen = 1
        activeSeqLen = 1
        sortedNums = sorted(nums)
        print(sortedNums)
        lastSeqNum = sortedNums[0]
        skipSeq = []
        i = 1
        while i < len(sortedNums):
            if sortedNums[i] == (lastSeqNum + 1):
                lastSeqNum = sortedNums[i]
                i += 1
                activeSeqLen += 1

            elif sortedNums[i] == lastSeqNum:
                skipSeq.append(i)
                i += 1
            else:
                activeSeqLen = 1
                lastSeqNum = sortedNums[i]
                i += 1            
            print(activeSeqLen)
            if activeSeqLen > longestSeqLen:
                longestSeqLen = activeSeqLen
        return longestSeqLen