#Problem: given a list of integers and a target, return the indecies of the integers that add up to target

#Initial solution: create a dictionary to store an (integer, index) pairs. Then iterate through the array and check to see if the needed compliment (target - nums[index]) exsists in the dictionary. if so, return the current index and the index in the dictionary. if not, create a new dictionary entry.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}

        for i in range(0, len(nums)):
            if (target - nums[i]) in dict.keys():
                return i, dict[target - nums[i]]
            else:
                dict[nums[i]] = i