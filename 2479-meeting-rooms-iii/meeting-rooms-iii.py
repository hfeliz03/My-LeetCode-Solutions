class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        available = list(range(n))          # free rooms by smallest index
        heapq.heapify(available)
        
        busy = []                           # (end_time, room)
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free all rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                finished_end, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                # Delay: take the room that frees earliest
                finished_end, room = heapq.heappop(busy)
                new_end = finished_end + duration
                heapq.heappush(busy, (new_end, room))
                count[room] += 1
        
        # Return room with max meetings; tie -> smallest index
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i