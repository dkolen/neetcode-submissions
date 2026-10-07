class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def binarySearch(nums, l, r, val):
            while l < r:
                idx = l + r // 2
                if nums[idx] == val:
                    return idx
                if nums[idx] < val:
                    l = idx
                else:
                    r = idx
            return -1
            
        res = []

        nums = sorted(nums)
        cur = len(nums) - 1
        while cur >= 2 and nums[cur] >= 0:
            val = nums[cur]
            l, r = 0, cur - 1
            while l < r:
                total = nums[l] + nums[r]
                if total + val == 0:
                    res.append([nums[l], nums[r], val])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                if total + val > 0:
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                if total + val < 0:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            cur -= 1
            while cur >= 2 and nums[cur] == nums[cur + 1]:
                cur -= 1 
        return res

    

