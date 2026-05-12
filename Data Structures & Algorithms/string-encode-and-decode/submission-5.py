class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return str(None)
        else:
            encoded = ";".join(strs)
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == str(None):
            return []
        else:
            decoded = s.split(sep=';')

        return decoded