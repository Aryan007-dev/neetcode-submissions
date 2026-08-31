
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tC = Counter(t)
        window = Counter()

        l = 0
        have = 0
        need = len(tC)

        res = ""
        resLen = float("inf")

        for r in range(len(s)):

            if s[r] in tC:
                window[s[r]] += 1

                if window[s[r]] == tC[s[r]]:
                    have += 1

            while have == need:

               
                if (r - l + 1) < resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                
                if s[l] in tC:
                    if window[s[l]] == tC[s[l]]:
                        have -= 1

                    window[s[l]] -= 1

                l += 1

        return res



                
                

        