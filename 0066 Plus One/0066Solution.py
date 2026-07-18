class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number=""
        for digit in digits:
            number+=str(digit)
        actual=int(number)+1
        return [int(x) for x in str(actual)]
