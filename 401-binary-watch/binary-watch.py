class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for h in range(12): 
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    m = str(m)
                    m = m if len(m) > 1 else "0" + m
                    res.append(str(h) + ':' + m)

        return res