class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _duplicate_set = set()
        _non_duplicate_set = set()
        for num in nums:
            if num not in _non_duplicate_set:
                _non_duplicate_set.add(num)
            else:
                _duplicate_set.add(num)

        if _duplicate_set:
            return True
        return False