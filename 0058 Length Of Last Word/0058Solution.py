class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split() # separate the words
        return len(words[len(words)-1]) # first get the last word in the list, then get the length of the last word and return its length
      #Runtime=0ms
        
