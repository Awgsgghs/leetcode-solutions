class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, curr):
            if idx == len(digits):
                res.append(curr[:])
                return
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, curr + letter)

        res = []
        backtrack(0, "")
        return res