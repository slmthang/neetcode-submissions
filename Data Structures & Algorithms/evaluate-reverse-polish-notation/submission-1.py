class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = '+-*/'
        stack = []

        for i in range(len(tokens)):
            
            if (tokens[i] in operators):
                sec_op = int(stack.pop())
                first_op = int(stack.pop())

                stack.append(self.calculate(first_op, sec_op, tokens[i]))
            else:
                stack.append(tokens[i])
        
        return int(stack.pop())

    def calculate(self, n1, n2, op):

        match op:
            case '+': return n1 + n2
            case '-': return n1 - n2
            case '*': return n1 * n2
            case '/': return n1 / n2
            case _: raise ValueError(f"Unknown operator: {op_string}")
    