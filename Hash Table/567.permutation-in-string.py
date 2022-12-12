#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        s1 : input lower case string possible permutation of s2
        s2 : input lower case string

        Algorithm: Iterate through s1 and count the unicode mapped down to 0 - 25
        for the indices of the s1 and s2 string counts arrays.

        Iterate through the two arrays together counting the matched number of string counts
        at each index.

        Slide a window with a left and right pointer where r starts at the s1.length
        and l starts at the beginning of s2.

        Map the right character, increment it to include that character
        in the counts array and check if the count matches at that index
        between the two string counts arrays are equal.
        If equal then increment matches. If we overshot then decrement our matches

        Map the left character, decrement it to exclude that character in the
        counts array and check if the count matches at that index
        between the two string counts arrays. If we undershot the counts at that index
        then we can decrement our matches.

        time T(n) = O(n) -> Upper and lower bounded by iterating through the whole of s2 once
        space S(n) = O(1) -> We only store the whole of the counts arrays as integers

        '''
        # s1 = s1.lower()
        # s2 = s2.lower()

        # convert strings to arrays to be index accessible 
        s1 = list(s1)
        s2 = list(s2)

        # check base case to make sure s2 is longer than s1
        if len(s1) > len(s2) or len(s2) == 0:
            return False
        
        if len(s1) == 0:
            return True 

        s1Counts, s2Counts = [0] * 26, [0] * 26
        i = 0
        n = len(s1) - 1
        while i <= n:
            s1Counts[ord(s1[i]) - ord('a')] += 1
            s2Counts[ord(s2[i]) - ord('a')] += 1
            i += 1
        
        matches = 0
        i = 0
        n = 26 - 1 # number of chars in lower case alphabet
        while i <= n:
            if s1Counts[i] == s2Counts[i]:
                matches += 1
            i += 1
        
        l = 0
        r = len(s1)
        n = len(s2) - 1 # we want this to be an integeer so wer only calaculate this length once
        # for the loop termination condition
        while r <= n:
            if matches == 26:
                return True
            
            # add chars from right of window
            index = ord(s2[r]) - ord('a')
            s2Counts[index] += 1            
            if s1Counts[index] == s2Counts[index]:
                matches += 1
            elif s1Counts[index] + 1 == s2Counts[index]: # made counts too large
                matches -= 1

            # remove chars from left of window
            index = ord(s2[l]) - ord('a')
            s2Counts[index] -= 1            
            if s1Counts[index] == s2Counts[index]:
                matches += 1
            elif s1Counts[index] - 1 == s2Counts[index]: # made counts too small
                matches -= 1                
            
            # increment l and r
            r += 1
            l += 1
        return matches == 26 # check after exiting loop once more






# @lc code=end

