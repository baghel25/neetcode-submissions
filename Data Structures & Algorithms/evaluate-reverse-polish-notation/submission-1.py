
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []
        arth = ["+", "-", "/", "*"]

        for i in range(len(tokens)):
            elm = tokens[i]

            if elm in arth:
                elm2 = res.pop()
                elm1 = res.pop()

                if elm == "+":
                    res.append(elm1 + elm2)
                elif elm == "-":
                    res.append(elm1 - elm2)
                elif elm == "*":
                    res.append(elm1 * elm2)
                elif elm == "/":
                    res.append(int(elm1 / elm2))
            else:
                res.append(int(elm))

        return res[0]
