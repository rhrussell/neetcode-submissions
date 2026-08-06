class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        # else:
        #     stack = []

        #     for char in s:
        #         if char == "[" or char == "(" or char == "{":
        #             stack.append(char)
        #         else:
        #             if len(stack) > 0:
        #                 open_char = stack.pop()

        #                 if open_char == "[" and char != "]":
        #                     return False
        #                 elif open_char == "(" and char != ")":
        #                     return False
        #                 elif open_char == "{" and char != "}":
        #                     return False
        #             else:
        #                 return False
                
        #     if len(stack) > 0:
        #         return False
        #     else:
        #         return True


                stack = []
                closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

                for c in s:
                    if c in closeToOpen:
                        if stack and stack[-1] == closeToOpen[c]:
                            stack.pop()
                        else:
                            return False
                    else:
                        stack.append(c)
                
                return True if not stack else False