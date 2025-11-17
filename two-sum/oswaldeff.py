class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_pairs = [(value, idx) for idx, value in enumerate(nums)]
        sorted_pairs.sort(key=lambda x: x[0])

        left, right = 0, len(nums) - 1

        while left < right:
            left_val, left_idx = sorted_pairs[left]
            right_val, right_idx = sorted_pairs[right]
            s = left_val + right_val

            if s == target:
                return [left_idx, right_idx]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []
