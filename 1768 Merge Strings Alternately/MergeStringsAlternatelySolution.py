class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_word=[]
        if len(word1)==len(word2):
            for letter in range(len(word2)):
                merged_word.append(word1[letter])
                merged_word.append(word2[letter])
            s="".join(merged_word)
            return s 

        if len(word1)>len(word2):
            for letter in range (len(word2)):
                merged_word.append(word1[letter])
                merged_word.append(word2[letter])
            merged_word.append(word1[len(word2):])
            s="".join(merged_word)
            return s
        elif len(word1)<len(word2):
            for letter in range (len(word1)):
                merged_word.append(word1[letter])
                merged_word.append(word2[letter])
            merged_word.append(word2[len(word1):])
            s="".join(merged_word)
            return s
        
