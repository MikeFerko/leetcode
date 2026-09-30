#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (49.04%)
# Likes:    8179
# Dislikes: 496
# Total Accepted:    935.8K
# Total Submissions: 1.9M
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
# 
# 
# 
# Example:
# 
# 
# Input
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
# 
# 
#

# @lc code=start
class WordDictionary:
    """
    Store words and search them with ``.`` wildcard support.
    """

    def __init__(self):
        """
        Initialize an empty word dictionary.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Add a word to the dictionary.

        Args:
            word: The lowercase word to add.

        Returns:
            None.

        @complexity: 
            Time complexity: T(word) = O(len(word)) time and O(len(word)) space.
            Space complexity: S(word) = O(len(word)) space.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        """
        Check whether a word or wildcard pattern is stored.

        Args:
            word: A lowercase pattern where ``.`` matches any one letter.

        Returns:
            True if a stored word matches the pattern; otherwise, False.

        @complexity: 
            Time complexity: T(word) = O(26 ** d * len(word)) time
            Space complexity: S(word) = O(len(word)) space,
            where ``d`` is the number of dots in ``word``.
        """
        def dfs(node, idx):
            if idx == len(word):
                return "$" in node

            ch = word[idx]
            if ch != ".":
                if ch not in node:
                    return False
                return dfs(node[ch], idx + 1)

            for next_node in node.values():
                if isinstance(next_node, dict) and dfs(next_node, idx + 1):
                    return True
            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

