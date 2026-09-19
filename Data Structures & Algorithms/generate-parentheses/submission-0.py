# Thoughts:
# Ok so first of all lets ask "what makes a parentheses pair valid?" 
# Well, for every opened ( there needs to be a )
# also actually that means no. of `(` == no. of `)`
# we always need to start with ( btw

# search space
#               (
#           /       \
#         (            )
#       /   \         / \
#      (     )       (   )
#      |    / \
#      )   (   )
#      |   |
#      )   )
#      |
#      )

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def explore(curr_str, open_count, close_count):
            if open_count == close_count == n:
                out.append(curr_str)
                return 

            # consider adding more "("
            if open_count < n:
                explore(curr_str + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                explore(curr_str + ")", open_count, close_count + 1)
                
        explore("", 0, 0)
        return out


