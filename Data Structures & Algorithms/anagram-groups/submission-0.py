from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for wrd in strs:
            ans = [0] * 26 
            for letter in wrd:
                ans[ord("a")-ord(letter)] += 1

            ana[tuple(ans)].append(wrd)
        
        return list(ana.values())