class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        total_count = len(nums)
        unique_count = len(set(nums))

        if total_count != unique_count:
            return True
        
        return False
