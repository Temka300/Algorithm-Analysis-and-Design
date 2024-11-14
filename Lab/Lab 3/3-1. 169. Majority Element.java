class Solution {
    public int majorityElement(int[] nums) {
        return helper(nums, 0, nums.length)[0];
    }

    private int[] helper(int[] nums, int l, int r) {
        if (l == r - 1) {
            return new int[]{nums[l], 1};
        }
        int mid = l + (r - l) / 2;
        int[] leftResult = helper(nums, l, mid);
        int[] rightResult = helper(nums, mid, r);

        int maj, extra;
        if (leftResult[0] == rightResult[0]) {
            maj = leftResult[0];
            extra = leftResult[1] + rightResult[1];
        } else if (rightResult[1] > leftResult[1]) {
            maj = rightResult[0];
            extra = rightResult[1] - leftResult[1];
        } else {
            maj = leftResult[0];
            extra = leftResult[1] - rightResult[1];
        }
        return new int[]{maj, extra};
    }
}