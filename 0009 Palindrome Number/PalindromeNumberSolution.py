class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x) #converts the integer into a string
        if x==x[::-1]: # if every number from left to right is he same as every number from right to left 
            return True # return true since it is a palindrome
        else:
            return False #otherwise return false
