#Problem: given a string of parenthesis type (), [], or {}, return true or false. Requirements: parenthesis open/close in a valid order, and there are no unpaired parenthesis.

# '({})' is valid, '()[]{}' is valid
#'({[}])' is invalid, '[)' is invalid

#Initial thoughts: parenthesis can be 'inside' of one another, so a stack would make sense. Use a dictionary to store a parenthesis' complement characters, and add/remove them from stack as needed. Once entire string has been exhausted, check to see if stack is empty. If it is, then return true.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s: #for each character in string
            if bracket in pairs: #if char is an opening bracket
                stack.append(bracket) #add bracket to stack
            elif len(stack) == 0 or bracket != pairs[stack.pop()]: #if its a closing bracket, it needs to be the complement of stack bracket
                return False

        return len(stack) == 0 #return true if nothing left in stack