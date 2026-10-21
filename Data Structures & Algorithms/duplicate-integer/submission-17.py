class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = []

        for n in nums:
            if n in hmap:
                return True
            hmap.append(n)

        return False