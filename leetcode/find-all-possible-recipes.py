class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        search_status = [0]*n # -1 = invalid, 0 = not searched, 1 = valid
        requirements = [[] for _ in range(n)]
        for i in range(n):
            for ingredient in ingredients[i]:
                if ingredient in recipes:
                    requirements[i].append(recipes.index(ingredient))
                elif ingredient not in supplies:
                    search_status[i] = -1
                    break
                    
            #print(requirements[i])
                    
        def dfs(node: int) -> int:
            nonlocal n, search_status, requirements
            #print(node, search_status)
            if search_status[node] == 0:
                search_status[node] = -1 # cycle detection
                for requirement in requirements[node]:
                    if dfs(requirement) == -1:
                        return search_status[node]

                search_status[node] = 1

            return search_status[node]        


        for i in range(n):
            dfs(i)

        return [recipes[i] for i in range(n) if search_status[i] == 1]
