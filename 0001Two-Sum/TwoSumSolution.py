class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={} #val:index
        for index,element in enumerate(nums):
            diff=target-element
            if diff in map:
                return [map[diff],index]
            map[element]=index
        return   #Runtime 0 ms
