class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """

        n=str(n)  #convert to str
        digit_list=list(n) #we split the number into a list of strings
        int_digit_list=[] 
        digit_product=1
        for digit in digit_list:
            int_digit_list.append(int(digit)) #we convert each digit to an integer and add them to the int digit list
            digit_product*=(int(digit))  # we multiply the int digit by the product
        digit_sum=sum(int_digit_list) #sum of digits
        total_sum=digit_sum+digit_product #total sum
        if int(n)%total_sum==0: #if the integer version of the number n is divisble by the total_sum
            return True #return true 
        return False #if not we return false
