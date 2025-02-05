class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        for num in nums: #O(n)
            if num not in dup_dict: #O(1)
                dup_dict[num] = 1
            else:
                return True
        return False
         
#Time complexity - O(n)
#Space complecity - O(n)
