# Asymmetrik-Mobile-Device-Keyboard
This is my implementation of the Mobile Device Keyboard programming challenge by Asymmetrik.
This solution was written in Python, using the tkinter GUI interface.

## Interface Specification
Candidate
    String getWord() : returns the autocomplete candidate
    Integer getConfidence() : returns the confidence* for the candidate

AutocompleteProvider
    PriorityQueue<Candidate> getWords(String fragment) : returns list of candidates ordered by confidence*
    void train(String passage) : trains the algorithm with the provided passage

## Technical Description
The core data structure used to represent autocomplete candidates is the Trie.
When a new passage is submitted for training, the passage is parsed into individual words,
converted into a Candidate object, and inserted into the Trie.
Time Complexity: O(m), where m is the length of the submitted passage.
Space Complexity: O(m)
  In the worst case, each word in the passage is unique, and new TrieNodes
  will be added to the root.

When entering a sentence fragment, we navigate to the corresponding node, if it exists, and
perform a BFS from that position, collecting all the paths to leaf nodes to find our candidates.
Time Complexity: O(n), where n is the number of nodes in the Trie
  In the worst case, every path in the Trie will be collected, but each node is only visited once.
Space Complexity: O(n)
  In the worst case, we store every node in our BFS queue once.

Once all candidates are collected, the results are sorted by their confidence, and then lexicographically,
and displayed in a Label widget.
Time Complexity: O(nlog(n)), where n is the number of nodes in the Trie
  In the worst case, every word is collected, and Python's default sort function implements a variation of TimSort,
  which runs on the order of nlog(n).
  Note: Alternatives here are placing results in a heap and heapifying the result, which also runs in
  O(nlog(n)) time.
Space Complexity: O(n)

## To run the code:
1. Download the code: https://github.com/byxng/Asymmetrik-Mobile-Device-Keyboard
2. Navigate to the main directory: cd Asymmetrik-mobile-device-keyboard
3. Install requirements: pip install -r requirements.txt
4. Run MobileKeyboardGUI: python Asymmetrik-mobile-device-keyboard/MobileKeyboardGUI.py
