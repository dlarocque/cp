class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix, suffix = [n+1]*(n+1), [n+1]*n
        
        # prefix sum
        running_sum = 0
        left, right = 0,0
        while right < n:
            running_sum += arr[right]
            while running_sum > target and left < right:
                running_sum -= arr[left]
                left += 1
                
            if running_sum == target:
                if right > 0:
                    prefix[right+1] = min(prefix[right-1], right-left+1)
                else:
                    prefix[right+1] = right-left+1
            elif right > 0:
                prefix[right+1] = min(prefix[right-1], prefix[right])
                    
            right += 1

        # suffix sum
        running_sum, left, right = 0,n-1,n-1
        while left >= 0:
            running_sum += arr[left]
            while running_sum > target and right > left:
                running_sum -= arr[right]
                right -= 1
            
            if running_sum == target:
                print(right, left)
                if left < n-1:
                    suffix[left] = min(suffix[left+1], right-left+1)
                else:
                    suffix[left] = right-left+1
            else:
                suffix[left] = min(suffix[right-1], suffix[right])
                
            left -= 1
            
        # find smallest non overlapping sub-arrays
        min_sum = 2*n
        
        for i in range(n):
            if prefix[i] <= n and suffix[i] <= n:
                min_sum = min(min_sum, prefix[i] + suffix[i])
             
        if min_sum == 2*n:
            return -1
            
        return min_sum
        
        
            
