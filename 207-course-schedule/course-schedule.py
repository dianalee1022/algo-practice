class Solution:

    def dfs(self, course, courseToPrereqs, visited) -> bool:
        # -1 visiting - prereq conflict
        # 1 visited - no prereq conflict
        if visited[course] == -1:
            return False

        if visited[course] == 1:
            return True
        
        visited[course] = -1

        for prereq in courseToPrereqs[course]:
            if not self.dfs(prereq, courseToPrereqs, visited):
                return False
        
        visited[course] = 1
        return True

        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)
        
        for course in range(numCourses):
            if not self.dfs(course, courseToPrereqs, visited):
                return False
        
        return True