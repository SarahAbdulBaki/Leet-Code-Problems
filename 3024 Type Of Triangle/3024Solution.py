class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)!=3: # if it doesnt have three sides it is not a triangle.
            return None
        if (nums[0]+nums[1]>nums[2]) and (nums[1]+nums[2]>nums[0]) and (nums[0]+nums[2]>nums[1]): #triangle inequality theorem
            if nums[0]==nums[1]==nums[2]: #if all equal then its an equilateral triangle
                return ("equilateral")
            elif nums[0]==nums[1] or nums[1]==nums[2] or nums[0]==nums[2]: # if at least two sides are equal it is an isosceles triangle
                return ("isosceles")
            elif nums[0]!=nums[1]!=nums[2]: #if none of the sides are equal it is a scalene triangle
             return ("scalene")
        return "none" # if the 3 sides do not meet the triangle inequality theorem then we return none
            
