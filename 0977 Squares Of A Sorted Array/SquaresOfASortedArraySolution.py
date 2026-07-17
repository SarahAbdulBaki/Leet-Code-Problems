class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_array=[]
        for num in nums:
            squared_array.append(num**2)
        (squared_array).sort()
        return squared_array
