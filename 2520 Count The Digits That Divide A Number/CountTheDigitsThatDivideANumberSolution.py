class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter=0
        num=str(num)
        for digit in num:
            if int(num)%int(digit)==0:
                counter+=1
        return counter #Runtime 0ms
