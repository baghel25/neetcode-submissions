
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_posi = max(piles)
        l = 1
        r = max_posi
        result = r

        while l <= r:
            m = (l + r) // 2
            sumOfpile = 0

            for elm in piles:
                sumOfpile += math.ceil(elm / m)

            if sumOfpile <= h:
                result = min(m, result)
                r = m - 1
            else:
                l = m + 1

        return result
