class Solution:
    def letEval(self, expression, scope): 
        scope[expression[0]] = self.genEval(expression[1], scope)
        return scope 
    def addEval(self, expression, scope): 
        return self.genEval(expression[1], scope) + self.genEval(expression[2], scope)
    def multEval(self, expression, scope): 
        return self.genEval(expression[1], scope) * self.genEval(expression[2], scope)
    def genEval(self, expression, scope): 
        if type(expression) != list: 
            try: 
                return int(expression)
            except: 
                return scope[expression]
        else: 
            if expression[0] == "let":
                expression = expression[1:]
                while len(expression) > 2: 
                    scope = self.letEval(expression, scope.copy())
                    expression = expression[2:]
                return self.genEval(expression[0], scope.copy())
            elif expression[0] == "add": 
                return self.addEval(expression, scope.copy())
            elif expression[0] == "mult":
                return self.multEval(expression, scope.copy())
    def evaluate(self, expression: str) -> int:
        stack = []
        par_end = {}

        for idx, ch in enumerate(expression):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                par_end[stack.pop()] = idx 

        def parse(lo, hi): 
            arr = []
            word = []

            i = lo 
            while i < hi: 
                if expression[i] == "(": 
                    arr.append(parse(i+1, par_end[i]))
                    i = par_end[i]
                elif expression[i] == " " or expression[i] == ")" and word != []:
                    if ''.join(word) != '':
                        arr.append(''.join(word))
                    word = []
                    i += 1 
                elif expression[i] != ")":
                    word.append(expression[i])
                    i += 1 
                else: 
                    i += 1 

            if word != []: 
                arr.append(''.join(word))

            return arr 

        expression_list = parse(1, len(expression)-1)
        return self.genEval(expression_list, {})


if __name__ == "__main__": 
    s = Solution()

    expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
    assert s.evaluate(expression) == 14 