class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0
        for op in operations:
            if op == '+':
                total += res[-2]+res[-1]
                res.append(res[-2]+res[-1])
            elif op == 'C':
                total -= res.pop()
            elif op == 'D':
                total += res[-1]*2
                res.append(res[-1]*2)
            else:
                total += int(op)
                res.append(int(op))
        
        return total