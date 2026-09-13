class Solution:
    def largestOverlap(self, img1, img2):
        ones1 = []
        ones2 = []

        n = len(img1)

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))

                if img2[r][c] == 1:
                    ones2.append((r, c))

        shifts = defaultdict(int)

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] += 1

        return max(shifts.values(), default=0)