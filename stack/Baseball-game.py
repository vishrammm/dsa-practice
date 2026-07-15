class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        
        for op in operations:
            if op == "+":
                # Add the sum of the last two scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Double the last score
                stack.append(stack[-1] * 2)
            elif op == "C":
                # Remove the last score
                stack.pop()
            else:
                # Convert the string integer to an actual int and record it
                stack.append(int(op))
                
        return sum(stack)