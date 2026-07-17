class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_dollar_bills=0 # making a counter for each type of bill we have
        ten_dollar_bills=0
        twenty_dollar_bills=0
        for bill in bills: # going through array of bills
            if bill==5:
                five_dollar_bills+=1 #no need to worry about change we just add to the counter
            elif bill==10:
                if five_dollar_bills>=1:# if we have at least 1, 5 dollar bill we can make the change
                    ten_dollar_bills+=1
                    five_dollar_bills-=1
                else:
                    return False # if we dont have enough five dollar bills we return false
            elif bill==20:
                
                if five_dollar_bills>=3 and ten_dollar_bills==0: #we do check one
                    twenty_dollar_bills+=1
                    five_dollar_bills-=3
                elif ten_dollar_bills>=1 and five_dollar_bills>=1:# and we do check two
                    twenty_dollar_bills+=1
                    ten_dollar_bills-=1
                    five_dollar_bills-=1
                # we do two checks since we can return change in two ways, first way being able to return 15 dollars as 3 fives, and second check being able to return 1 ten dollar bill and 2 fives
                else:
                    return False
        return True    # if we are able to return the correct amount of change we return true
        
