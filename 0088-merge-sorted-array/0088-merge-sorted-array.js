/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let index1 = m - 1; // Last index of nums1 that is part of the merge
    let index2 = n - 1; // Last index of nums2
    let mergeIndex = m + n - 1; // Last index of nums1 array

    while (index2 >= 0) {
        if (index1 >= 0 && nums1[index1] > nums2[index2]) {
            nums1[mergeIndex] = nums1[index1];
            index1--;
        } else {
            nums1[mergeIndex] = nums2[index2];
            index2--;
        }
        mergeIndex--;
    }
};