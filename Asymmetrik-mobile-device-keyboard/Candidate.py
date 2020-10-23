

class Candidate:
    def __init__(self, word):
        self.word = word
        self.confidence = 1  # confidence value initialized as 1

    def __str__(self):
        """
        Format candidate output
        """
        return '\"{self.word}\" ({self.confidence})'.format(self=self)

    def getWord(self):
        """
        Returns the autocomplete candidate
        """
        return self.word

    def getConfidence(self):
        """
        Returns the confidence * for the candidate
        """
        return self.confidence

    def incrementConfidence(self):
        self.confidence += 1
