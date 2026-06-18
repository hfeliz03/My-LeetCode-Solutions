class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 30 mins == 15 degrees
        # 15 mins == 7.5
        degMins = minutes * 6
        degHours = (hour%12) * 30 + (minutes/2) 
        print(f"{degMins=}, {degHours=}")
        return min(max(degMins, degHours) - min(degMins, degHours), max(360-degMins, degHours) + min(360-degMins, degHours), max(degMins, 360-degHours) + min(degMins, 360-degHours))