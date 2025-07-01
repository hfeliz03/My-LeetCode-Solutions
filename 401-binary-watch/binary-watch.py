class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8 : return []
        
        res = []
        for h in range(12): #hours from [0,11] max 3 1's
            for m in range(60): #minutes from [0,59] max 5 1's
                if bin(h).count('1') + bin(m).count('1') == turnedOn: 
                    res.append(f"{h}:{m:02d}")
        return res