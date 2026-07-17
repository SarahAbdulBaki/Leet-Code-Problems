class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)<26:
            return False
        alphabets="thequickbrownfoxjumpsoverthelazydog"
        for letter in alphabets:
            if letter not in sentence:
                return False
        return True
    
            
