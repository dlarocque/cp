class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """
        Create a topological sort of nums
        for all subsequences
            traverse topological sort with subsequence
            if there are elements left in subsequence, but we've hit the end of the topological sort,
                return False

        return True

        """
        # Create an adjacency list
        
