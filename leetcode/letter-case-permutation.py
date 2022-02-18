class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        DFS where we search for all of the permutations of strings
        where at each level we change the casing of one letter
        
        Dynamic programming:
        - Use previously computed permutations, and build upon those
        
        s = 'a1b2'
        
        if char is letter:
            for permutation in permutations of string ending before current char
                append lowercase to all
                append uppercase to all
        else
            for permutation in permutations of stirng ending before current char
                append number to all
            
        
        Note:
        1. A letter gives us two choices (permutations), lowercase and uppercase
        2. A number gives us one choice (permutation)
        
        
        """
        permutations = ['']
        
        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                # casing matters!
                for idx, permutation in enumerate(permutations[:]):
                    permutations[idx] = permutation+char
                    if char.islower():
                        permutations.append(permutation+char.upper())
                    else:
                        permutations.append(permutation+char.lower())
            else:
                # casing does not matter
                for idx, permutation in enumerate(permutations):
                    permutations[idx] = permutation+char
                    
        return permutations
