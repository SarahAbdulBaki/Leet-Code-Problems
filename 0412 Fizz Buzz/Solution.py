class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arrayy=[]
        for i in range (1,n+1):
            if ((i%3)==0) and ((i%5)==0):
                arrayy.append("FizzBuzz")
            elif i%5==0:
                arrayy.append("Buzz")
            elif i%3==0:
                arrayy.append("Fizz")
            else:
                arrayy.append(str(i))
        return arrayy
