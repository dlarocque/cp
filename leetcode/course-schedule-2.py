class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Graph problem
        - 0...numCourses vertices
        - prerequisites edges

        We can't complete all of the courses if we can't complete all of the prerequisites.
        When can't we complete all of the prerequisites?
            When there exists a prerequisite for a course that requires the course we are trying to complete.
            (cycle in the prerequisites)

        Perform cycle-detection to see if we can complete all of the courses.
        > Is there an order of courses s.t. we can complete all of the courses
        Directed graph ordering => Topological sort

        Notes:
            A graph can be ordered in a topological sort iff the graph is acyclic.

        If we can create a topological sort of the graph, return True.

        Algorithm for creating topological sort:
            processing, processed: set()
        """
        processing, processed = set(), set()
        course_order = []

        # Create an adjacency list
        prereqs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)


        def dfs(course: int) -> bool:
            """Returns false if there is a cycle in the search"""
            nonlocal course_order
            if course in processing:
                # print("Cycle detected at ", course)
                return False
            
            if course in processed:
                return True

            processing.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            processing.remove(course)
            processed.add(course)
            course_order = [course] + course_order
            return True
        

        for course, _ in prerequisites:
            if course in processed:
                continue
            if not dfs(course):
                return False

        # print("Topological Sort: ", course_order)
        return True
