class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """
        number of divisors of with k digits
        
        read through substrings of str(num) len k
        """
        str_num = str(num)
        res = 0
        for left in range(len(str_num)-k+1):
            if int(str_num[left:left+k]) != 0 and num % int(str_num[left:left+k]) == 0:
                res += 1
                        
        return res
