class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        total_y=0
        total_x=0
        for move in moves:
            if move=="U":
                total_y+=1
            elif move=="D":
                total_y-=1
            elif move=="L":
                total_x+=1
            elif move=="R":
                total_x-=1
        if total_y==total_x==0:
                return True
        return False
            
        
