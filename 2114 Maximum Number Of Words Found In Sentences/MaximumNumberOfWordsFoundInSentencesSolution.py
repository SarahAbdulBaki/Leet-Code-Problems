class Solution(object):
    def mostWordsFound(self,sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(len(word.split()) for word in sentences) #count the number of words in each sentence , then find the sentence with the maximum amount of words
