class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #push each number to stack
        # when we reach op, pop 2 nums from stack and perform the op
        #push the res back to stack
        stack = []

        for n in tokens:
            if n in {"+", "-", "*", "/"}:
                num2 = stack.pop()
                num1 = stack.pop() # Goes on right side of op
                
                if n == "+":
                    stack.append((num1 + num2))
                elif n == "-":
                    stack.append((num1 - num2))
                elif n == "*":
                    stack.append((num1 * num2))
                elif n == "/":
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(n))

        return stack[0]




                