#Problem: given a roman numeral (string type), convert it into an integer and return the value

#Initial thoughts: use a dictionary to associate characters with values

#Possible problems: roman numerals read from left to right, but left-relative values can subtract from the total sum if preceeding other certain values

#Pattern: values are only ever subtracted if the current index is less than the next index

#Solution: create a dictionary to store values to characters. Set sum variable to zero and iterate through string, checking each index with the next to make sure the current index will get added to the sum, not subtracted. Include a check to make sure the last index doesn't try to find the index after itself.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = { #initializing map
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0 #setting sum

        for i in range(0, len(s)): #iterating through string
            if i != len(s) - 1: #last index check
                if values[s[i]] < values[s[i+1]]: #concurrent index comparison
                    sum -= values[s[i]]
                else:
                    sum += values[s[i]]
            else: #if last index, add
                sum += values[s[i]]
        return sum