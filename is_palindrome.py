#Problem: given an integer, return true/false on if integer is palindrome (does number read left-right as it does right-left)

#Initial thoughts: convert int to string. create two iterators pointing at each end of string. While iterators have not reached the middle, compare them. if they're the same, incriment/decrement accordingly. once while loop has executed, return true, return false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        p1 = 0
        p2 = len(x) - 1

        while p1 < p2:
            if x[p1] == x[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True