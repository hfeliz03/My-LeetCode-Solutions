class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText: return encodedText
        # 0,0 0,1 0,2 0,3 0,4 0,5
        # ""  1,1 1,2 1,3 1,4 1,5
        #                     2,5
        #
        # 0  1  2  3  4  5
        # 6  7  8  9  10 11
        # 12 13 14 15 16 17
        # 18 19 20 21 22 23

        #iveo__
        #__eed_
        #__l_t_
        #___olc
        #The last element is the highest character in the last column 

        #0 1 2  3
        #4 5 6  7
        #8 9 10 11



        #Add the character at m+n. If we do m steps then that means we have to go back to the start of "a new col"
        #Stop when you reach the end of original text
        originalText = ""
        m, n = rows, len(encodedText)//rows
        # #find last character Unnecessary asl womp womp
        # for elementInLastCol in range(n-1,m*n,n):
        #     if encodedText[elementInLastCol] != " ":
        #         indexOfLastElement = elementInLastCol
        #         print(f"{elementInLastCol=}")
        #         print(f"{encodedText[elementInLastCol]=}")
        #         break
            
        for col in range(n):
            for row in range(m):
                i = col + (row*(n+1))
                if i >= len(encodedText): break
                originalText += encodedText[i]
        
        return originalText.rstrip()
