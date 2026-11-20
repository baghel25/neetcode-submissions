class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for elm in points:
            x, y = elm
            cal = x**2 + y**2
            res.append((cal, elm))

        res.sort(key=lambda x: x[0])

        return [m[1] for m in res[:k]]