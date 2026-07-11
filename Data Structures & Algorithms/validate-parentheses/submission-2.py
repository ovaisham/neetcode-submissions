from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        dq = deque([])
        while i < len(s):
            if i == 0 and not self.ifLeft(s[i]):
                return False
            elif self.ifLeft(s[i]):
                dq.append(s[i])
                i += 1
            else:
                if not dq:
                    return False
                else:
                    target = dq.pop()
                if s[i] == ')' and target == '(':
                    i += 1
                elif s[i] == ']' and target == '[':
                    i += 1
                elif s[i] == '}' and target == '{':
                    i += 1
                else:
                    return False
        if dq:
            return False
        else:
            return True

    def ifLeft(self, ch):
        if ch == '[' or ch == '{' or ch == '(':
            return True
        else:
            return False