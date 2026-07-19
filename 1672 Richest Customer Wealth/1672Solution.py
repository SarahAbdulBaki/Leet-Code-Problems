class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth=0
        sum=0
        for account in accounts:
            for money in account:
                sum+=money
            if sum>max_wealth or max_wealth==sum:
                max_wealth=sum
                sum=0
            sum=0 # if the sum isnt bigger then the max wealth we still need to reset it at the end
        return max_wealth
        
