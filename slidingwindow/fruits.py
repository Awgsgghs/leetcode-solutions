class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        mp = {}
        maxlength = 0
        for right in range(len(fruits)):
            mp[fruits[right]] = mp.get(fruits[right], 0) + 1
            while len(mp) > 2:
                mp[fruits[left]] -= 1
                if mp[fruits[left]] == 0:
                    del mp[fruits[left]]
                left += 1
            maxlength = max(maxlength, right - left + 1)
        return maxlength
