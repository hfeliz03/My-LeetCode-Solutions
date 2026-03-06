class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segmentDone = False
        for binary in s:
            if binary == "1" and segmentDone == False:
                continue
            elif binary != "1":
                segmentDone = True
            else:
                return False
        return True