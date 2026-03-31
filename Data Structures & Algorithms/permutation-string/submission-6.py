from collections import Counter,defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Consecutive letter but can be reordered
        # len(s2) >= len(s1)

        # We can go through s2 and keep a window of len(s1)
        # we can keep a count of the letters in the window
        # if at any point the window counts match s1 counts
        # return True
        # else return False

        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        c2 = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            c2[s2[r]] += 1

            if r - l + 1 > len(s1):
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1

            if c1 == c2:
                return True

        return False