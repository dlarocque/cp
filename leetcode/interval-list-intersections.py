class Solution:
    def intervalIntersection(self, first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
        """
        if firstStart <= secondEnd <= firstEnd
            there is an intersection from [max(firstStart, secondStart),secondEnd]

        if first secondEnd >= firstEnd
            the interval following second will not overlap with first
            interate over first
        else
            the interval following second could overlap with first
            iterate over second
        """
        intersections = []

        i, j = 0, 0
        while i < len(first_list) and j < len(second_list):
            a_start, a_end = first_list[i]
            b_start, b_end = second_list[j]
            # Check for an intersection
            if a_start <= b_end and b_start <= a_end:
                intersection_start = max(a_start, b_start)
                intersection_end = min(a_end, b_end)
                intersections.append([intersection_start, intersection_end])

            # Increment
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return intersections

