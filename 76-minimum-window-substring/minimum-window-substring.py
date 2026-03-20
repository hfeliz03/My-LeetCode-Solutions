from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Define t as a dictionary of frequencies. Identify if the current window contains all of t. if not keep growing
        # The windows will have a size of at least |t| 
        # For every substring, checking if all of the values of t are present will take O(|t|)
        # We dont need to check every possible window. the initial value of every window should be a value in t.
        # After you found a substring that contains all of t, move on, theres no point in increasing such window. 
        #if s == t: return t
        tFreqs = Counter(t)
        sFreqs = Counter(s)
        if dict(tFreqs & sFreqs) != tFreqs: return ""
        
        output = ""
        i = 0
        j = 0
        curMinWindow = float("inf")
        curSubstrFreq = Counter()

        while i < len(s):
            if s[i] not in tFreqs: 
                i+=1
                continue
            # grow window until it becomes valid or j reaches end
            while j < len(s) and dict(curSubstrFreq & tFreqs) != tFreqs:
                curSubstrFreq[s[j]] += 1
                j += 1

            # if current window is valid, update answer
            if dict(curSubstrFreq & tFreqs) == tFreqs:
                if j - i < curMinWindow:
                    curMinWindow = j - i
                    output = s[i:j]

            # shrink from left for next iteration
            curSubstrFreq[s[i]] -= 1
            if curSubstrFreq[s[i]] == 0:
                del curSubstrFreq[s[i]]
            i += 1

        return output