class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build dependency list
        graph = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        path = set()
        safe = set()

        def dfs(course):
            if course in path:
                return False
            if course in safe:
                return True
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            safe.add(course)
            path.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        







# numCourses = 4
# prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]

# # build some kind of a dependency list
# {
#     0: []
#     1: [0, 3],
#     2: [1],
#     3: [2],
# }

# 0 <- 1 -> 3
#      ^   /
#      |  /
#      2



