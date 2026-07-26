class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        have = {}
        number = len(need)
        left = 0
        minlength = len(s) + 10
        startid = -1
        for right in range(len(s)):
            have[s[right]] = have.get(s[right], 0) + 1
            if s[right] in need.keys() and have[s[right]] == need[s[right]]:
                number -= 1
            while number == 0:
                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    startid = left
                have[s[left]] -= 1
                if s[left] in need.keys() and have[s[left]] < need[s[left]]:
                    number += 1
                left += 1
        return s[startid:startid + minlength] if startid != -1 else ""

