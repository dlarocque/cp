import collections 
class Solution:
    def longestStrChain(self, words) -> int:
        n = len(words)
        words.sort() # sorts strings lexicographically
        words.sort(key=len)

        max_chain = [1]*n    
        def find_max_chain(i: int) -> None:
            if i >= n:
                return

            for j in range(i-1, -1, -1):
                if len(words[j]) == len(words[i])-1:
                    # check if predecessor
                    predecessor = False
                    idx_i, idx_j = 0, 0
                    while idx_j < len(words[j]):
                        if words[i][idx_i] != words[j][idx_j]:
                            if not predecessor:
                                predecessor = True
                                idx_i += 1
                            else:
                                predecessor = False
                                break
                        else:
                            idx_i += 1
                            idx_j += 1
                                
                    if predecessor or idx_j == len(words[j]):
                        max_chain[i] = max(max_chain[i], max_chain[j]+1)

                elif len(words[j]) < len(words[i])-1:
                    break

        for i in range(n):
            find_max_chain(i)
            
        print(max_chain)
            
        return max(max_chain)
