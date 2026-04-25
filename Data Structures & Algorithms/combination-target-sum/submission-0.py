class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrace(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrace(i, path, total + nums[i])
                path.pop()
        
        backtrace(0, [], 0)
        return res
        