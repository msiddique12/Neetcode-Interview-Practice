class Solution:
    def isValid(self, s: str) -> bool:
        #([{}])
        stack = []
        m = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                if not stack or stack.pop() != m[c]:
                    return False
        return len(stack) == 0

