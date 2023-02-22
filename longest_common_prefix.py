#Problem: given a list of strings, return the longest common prefix between them. Return None otherwise

#Initial thoughts: Search the strings vertically. Create a list of tuples containing the characters in a given index using the zip() function. Check for unique values using len(set()) and concat the prefix string if there are no unique values for a given index.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        index_tuples = zip(*strs) #creates list of tuples
        prefix = ""

        for index in index_tuples: #iterating through tuple list
            if len(set(index)) > 1: break #if there are unique values in tuple
            prefix += index[0] #otherwise add index char onto prefix var
        return prefix

