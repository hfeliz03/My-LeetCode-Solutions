class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for start, end, price in flights:
            graph[start].append((end, price))

        # (total_cost, current_city, flights_taken)
        frontier = [(0, src, 0)]

        # Track the fewest flights used when processing each city.
        min_flights = [float("inf")] * n

        while frontier:
            cost, city, flights_taken = heapq.heappop(frontier)

            if city == dst:
                return cost

            # k stops means at most k + 1 flights.
            if flights_taken == k + 1:
                continue

            if flights_taken >= min_flights[city]:
                continue

            min_flights[city] = flights_taken

            for neighbor, price in graph[city]:
                heapq.heappush(
                    frontier,
                    (cost + price, neighbor, flights_taken + 1)
                )

        return -1