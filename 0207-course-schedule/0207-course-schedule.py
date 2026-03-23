class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
    
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        state = [0] * numCourses
        # 0 = unvisited, 1 = visiting, 2 = done

        def dfs(course):
            if state[course] == 1:
                return False   # cycle
            if state[course] == 2:
                return True    # already processed safely

            state[course] = 1

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True