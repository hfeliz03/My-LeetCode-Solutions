class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for length in range(2, min(9, len(str(high))) + 1):
            curr = int("123456789"[:length])
            increment = int("1" * length)
            while curr <= high and str(curr)[-1] != "0":
                if curr >= low:

                    res.append(curr)
                curr += increment
        return res