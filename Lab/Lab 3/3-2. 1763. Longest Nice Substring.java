class Solution {
    public String longestNiceSubstring(String s) {
        String ans = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                String substring = s.substring(i, j);
                if (isNice(substring) && substring.length() > ans.length()) {
                    ans = substring;
                }
            }
        }
        return ans;
    }

    private boolean isNice(String s) {
        for (char c : s.toCharArray()) {
            if (!s.contains(Character.toString(Character.toLowerCase(c))) ||
                !s.contains(Character.toString(Character.toUpperCase(c)))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestNiceSubstring("YazaAay"));  // Output: "aAa"
    }
}