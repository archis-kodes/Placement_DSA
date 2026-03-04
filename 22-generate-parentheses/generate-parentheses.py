class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid_parenthesis(string):
            stack = []
            for i in string:
                if i=="(":
                    stack.append(i)
                else:
                    if stack and stack.pop()=="(":
                        continue
                    else:
                        return False
            return len(stack)==0

        def generate_paranthesis(n, string):
            if len(string)==n:
                if valid_parenthesis(string):
                    result.append(string)
                return
            # Choose Open
            generate_paranthesis(n, string+"(")
            generate_paranthesis(n, string+")")

        result = []
        generate_paranthesis(2*n, "")
        return result
