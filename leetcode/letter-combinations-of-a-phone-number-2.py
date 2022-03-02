class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 
        return all possible letter combinations that the number could represent

        Time: O(3^digits.length)
        """
        digit_to_letters = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'], 
            6: ['m','n','o'], 
            7: ['p','q','r','s'], 
            8: ['t','u','v'],
            9: ['w','x','y','z'],
        }

