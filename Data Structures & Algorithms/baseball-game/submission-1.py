# if operation is `x`, add to stack and scores
# if operation is `C`, remove from scores
# if operation is `+`, pop twice from stack and add sum to scores
# if operation is `D`, pop once from stack and add double to scores

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1]*2)
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(op))
        
        return sum(scores)