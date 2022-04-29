import collections
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        count the amount of unique characters in all substrings of s
        
        Notes:
        - There are n(n+1)/2 substrings of s
        - Some substrings may be repeated, in this case we re-count them 
        
        Algorithm for counting amount of unique characters in a substring t:
            Create a dictionary d
            count = 0
            for every char in t
                if d[char] == 0
                    d[char] = 1
                    count += 1
                else if d[char] == 1
                    d[char] = -1
                    count -= 1
        - O(n) time, O(n) space
        
        If we do this on all substrings in s
        - Time: O(n^3)
        - Space: O(n)

        How can we optimize?
        If we know a substring i...j has k unique characters
        If j+1 has freq == 0 in i...j
            i...j+1 has k+1 unique characters
        If j+1 has freq == 1 in i...j
            i...j+1 has k-1 unique characters
        If j+1 has freq > 1 in i...j
            i...j+1 has k unique characters
        
        Dynamic Programming
        Let's define the recurrence relation:
            count(s[i...j]) = {
                count(s[i...j-1])   if char at j has freq > 1 in s[i...j-1]
                count(s[i...j-1])-1 if char at j has freq == 1 in s[i...j-1]
                count(s[i...j-1))+1 if char at j has freq == 0 in s[i...j-1]
                1                   if i == j 
            }
            
        Time: O(n^2)
        Space: O(n^2)
        
        Can we bring this down to O(nlogn)? O(n)?
        - We would have to find a way to not visit all substrings
            
        Pseudocode:
        freq = dict
        count = 0
        dp = 2d array of size n*n
        for i in 0...n-1
            freq = {}
            f
            for j in i...n-1
            
        
        Input: "LEETCODE"

        """
        total_count, n, cnt = 0, len(s), 0
        for i in range(n):
            freq = collections.defaultdict(int)
            for j in range(i, n):
                match freq[s[j]]:
                    case 0:
                        freq[s[j]] = 1
                        cnt += 1
                    case 1:
                        freq[s[j]] = -1
                        cnt -= 1

                total_count += cnt

        return total_count
