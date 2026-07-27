class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        smap = {}
        for ch in s:
            smap[ch] =smap.get(ch,0)+1

        for ch in t:
            if ch not in smap:
                return False
            smap[ch]-=1

            if smap[ch] < 0:
                return False

        return True           


             