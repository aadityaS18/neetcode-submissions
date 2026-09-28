class Solution:
    def isValid(self, s: str) -> bool:

        bracket_mapping = {
    ")": "(",
    "]": "[",
    "}": "{"
}

        stack=[]
        for ch in s :
            if ch in bracket_mapping.values():#   # if it is an opening bracket
                #open:

                stack.append(ch)

            else:
                if stack and stack[-1]== bracket_mapping[ch]:#  # stack must not be empty
                # and top must match the required opening bracket
                    stack.pop()

                else:
                    return False
        return not stack 



            











        