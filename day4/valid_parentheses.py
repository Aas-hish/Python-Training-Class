class Solution(object):
    def isValid(self, s):
       stack =[]
       brackets={')':'(','}':'{',']':'['}
       for i in s:
        if(i in brackets.values()):
            stack.append(i)
        else:
            if(not stack or brackets[i] != stack.pop()):
                return False

       return len(stack) == 0
   

S =Solution()
print(S.isValid("(){}[]"))
print(S.isValid("(){[]"))
print(S.isValid("(){[}]"))