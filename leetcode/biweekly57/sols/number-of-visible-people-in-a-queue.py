class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        For each person in the list, a person can see the person next to them,
        `if stack: res[stack[-1]] += 1`

        If we find a person that is larger than a previous person, then we know that all
        of the people in between those two people can see that tall person.
        `while stack and heights[stack[-1]] <= v: res[stack.pop()] += 1`

        """
        res = [0] * len(heights)
        stack = []

        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)

        return re
