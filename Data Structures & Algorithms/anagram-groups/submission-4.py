class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for st in strs:
            temp = ''.join(sorted(st))
            group[temp].append(st)
        
        newList = list(group.values())
        return newList

        
