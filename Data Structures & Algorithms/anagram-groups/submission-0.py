class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        grpAna = {}
        for word in strs:
            wordSort = "".join(sorted(word))
            if wordSort in grpAna:
                grpAna[wordSort].append(word)
            else:
                grpAna[wordSort] = [word]
        for key in grpAna:
            output.append(grpAna[key])
        return output
        