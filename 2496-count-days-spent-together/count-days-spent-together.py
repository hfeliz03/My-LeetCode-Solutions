class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        leaveAlice = [int(leaveAlice[:2]), int(leaveAlice[3:])]
        leaveBob = [int(leaveBob[:2]), int(leaveBob[3:])]
        arriveAlice = [int(arriveAlice[:2]), int(arriveAlice[3:])]
        arriveBob = [int(arriveBob[:2]), int(arriveBob[3:])]


        Amonth, Aday = arriveAlice[0], arriveAlice[1]    
        Bmonth, Bday = arriveBob[0], arriveBob[1]    

        AliceArrivesFirst = -1 
        if Amonth < Bmonth:
            AliceArrivesFirst = 1
        elif Amonth > Bmonth:
            AliceArrivesFirst = 0
        else:
            if Aday <= Bday: 
                AliceArrivesFirst = 1
        
        AmonthLeave, AdayLeave = leaveAlice[0], leaveAlice[1]    
        BmonthLeave, BdayLeave = leaveBob[0], leaveBob[1]    

        AliceLeavesFirst = -1 
        if AmonthLeave < BmonthLeave:
            AliceLeavesFirst = 1
        elif AmonthLeave > BmonthLeave:
            AliceLeavesFirst = 0
        else:
            if AdayLeave <= BdayLeave: 
                AliceLeavesFirst = 1

        def getTimeDifference(arrival, departure):
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            res = 0
            while arrival[0] <= departure[0]:
                if arrival[0] < departure[0]:
                    res += months[arrival[0]-1] - arrival[1] +1
                else: #same month of arrival and departure
                    res += departure[1] - arrival[1] + 1
                arrival = [arrival[0]+1, 1]
            if res < 0: res = 0
            return res

        timeTogether = 0
        if AliceArrivesFirst == 1:
            firstDayTogether = arriveBob
            lastDayTogether = leaveAlice if AliceLeavesFirst == 1 else leaveBob
                
        else:
            firstDayTogether = arriveAlice
            lastDayTogether = leaveAlice if AliceLeavesFirst == 1 else leaveBob

        return getTimeDifference(firstDayTogether, lastDayTogether)


