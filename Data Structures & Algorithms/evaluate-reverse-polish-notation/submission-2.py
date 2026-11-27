class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        order = []
        for c in tokens:
            if c == "+":
                order.append(order.pop() + order.pop())
            elif c == "-":
                a, b = order.pop(), order.pop()
                order.append(b-a)
            elif c == "*":
                order.append(order.pop() * order.pop())
            elif c == "/":
                a, b = order.pop(), order.pop()
                order.append(int(b / a))
            else:
                order.append(int(c))
        
        return order[0]
            
