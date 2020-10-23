from collections import defaultdict, deque
from Trie import TrieNode
from string import punctuation
from Candidate import Candidate


class AutocompleteProvider:
    def __init__(self):
        # mapping of words to candidate objects
        self.candidate_dict = defaultdict(Candidate)
        self.root = TrieNode()  # root node for our Trie

    def insert(self, word, cur_candidate):
        """
        Insert a new word into our Trie
        """
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isEnd = True
        cur.candidate = cur_candidate

    def getWords(self, fragment):
        """
        Returns list of candidate objects ordered by confidence*
        Uses a BFS to traverse the nodes of the Trie from our current word
        fragment, and return the candidates sorted by confidence
        """
        candidates = []
        if not fragment:
            return []
        # navigate to the node making up our fragment, if it exists
        cur = self.root
        for letter in fragment:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return []

        # perform BFS on Trie leaves to find candidates
        queue = deque([cur])
        while queue:
            cur_node = queue.popleft()
            if cur_node.isEnd:
                candidates.append(cur_node.candidate)

            for ch in cur_node.children.values():
                queue.append(ch)

        # sort candidates by confidence and lexicographical order
        candidates = sorted(candidates, key=lambda x: -x.confidence)
        return candidates

    def train(self, passage):
        """
        Trains the algorithm with the provided passage by parsing the input
        text, adding each word to a Trie, and tracking confidence of each word
        in a hashmap.

        * Confidence is the likelihood/relevance of an individual word relative
        to the other words being returned by the autocomplete provider.
        If two words are equally likely, they should have the same confidence.
        If one is more likely, it should have a higher confidence.
        """
        # parse input passage
        for w in passage.split():
            temp = w.lower().strip(punctuation)
            # if our word already exists, increment confidence
            if temp in self.candidate_dict:
                cur_candidate = self.candidate_dict[temp]
                cur_candidate.incrementConfidence()
            # otherwise, add to dictionary
            else:
                self.candidate_dict[temp] = Candidate(temp)
                cur_candidate = self.candidate_dict[temp]
            self.insert(temp, cur_candidate)
