# https://leetcode.com/problems/remove-duplicate-letters/description/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l_dict = {}
        for l in s:
            if l in l_dict: l_dict[l] += 1
            else: l_dict[l] = 1

        res = []
        resflag = set()
        for l in s:
            l_dict[l] -= 1
            if l in resflag:
                continue
            while res and res[-1] > l and l_dict[res[-1]] > 0 and l not in resflag:
                resflag.discard(res[-1])
                res.pop()
            res.append(l)
            resflag.add(l)

        return ''.join(res)