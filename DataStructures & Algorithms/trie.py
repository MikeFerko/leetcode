'''
Trie (Prefix Tree)

A tree where each path from the root spells out a string, character by
character, and shared prefixes share the same path. Built for fast
"does this word exist" / "does anything start with this prefix" lookups
over a large set of strings -- much cheaper than scanning every word.

Time Complexity: T(n) = O(L) for insert/search/startsWith, where L is
the length of the word/prefix being processed -- independent of how
many words are already stored.
Space Complexity: S(n) = O(total characters stored across all words),
since shared prefixes are only stored once.
'''

class TrieNode:
    def __init__(self):
        # maps a single character -> the child TrieNode for that character
        self.children = {}
        # marks that some inserted word ends exactly at this node
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # create the branch for this character if it doesn't exist yet
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # mark the final node as a complete word, not just a prefix
        node.isEndOfWord = True

    def findNode(self, prefix: str):
        # walk down the tree one character at a time; bail out early
        # the moment a character isn't present
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        # the characters all existed AND some word was explicitly inserted here,
        # not just passing through as a prefix of a longer word
        return node is not None and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # just needs the path to exist -- doesn't matter if a full word ends here
        return self.findNode(prefix) is not None


# Driver code
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))     # True, exact word was inserted
    print(trie.search("app"))       # False, "app" was never inserted as its own word
    print(trie.startsWith("app"))   # True, "apple" starts with "app"

    trie.insert("app")
    print(trie.search("app"))       # True, now it has been inserted directly
