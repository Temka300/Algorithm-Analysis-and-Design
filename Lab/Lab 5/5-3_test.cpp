#include <iostream>
#include <cassert>
#include "5-3 Longest Common Subsequence.c++"

void testLongestCommonSubsequence() {
    Solution solution;

    // Test case 1: Both strings are empty
    assert(solution.longestCommonSubsequence("", "") == 0);

    // Test case 2: One string is empty
    assert(solution.longestCommonSubsequence("abc", "") == 0);
    assert(solution.longestCommonSubsequence("", "abc") == 0);

    // Test case 3: No common subsequence
    assert(solution.longestCommonSubsequence("abc", "def") == 0);

    // Test case 4: Some common subsequence
    assert(solution.longestCommonSubsequence("abcde", "ace") == 3);
    assert(solution.longestCommonSubsequence("abc", "abc") == 3);
    assert(solution.longestCommonSubsequence("abc", "defabc") == 3);

    // Test case 5: Complex case
    assert(solution.longestCommonSubsequence("abcbdab", "bdcaba") == 4);

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testLongestCommonSubsequence();
    return 0;
}
