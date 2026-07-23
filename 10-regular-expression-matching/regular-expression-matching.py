class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(curS, curP):
            if not curP: return not curS
            first_match = (bool(curS) and (curS[0] == curP[0] or curP[0] == "."))

            # Current pattern character is followed by '*'
            if len(curP) >= 2 and curP[1] == "*":
                return (
                    helper(curS, curP[2:])  # Use 0 occurrences
                    or 
                    (first_match and helper(curS[1:], curP))  # Use 1+ occurrences
                )

            return first_match and helper(curS[1:], curP[1:])

        return helper(s, p)