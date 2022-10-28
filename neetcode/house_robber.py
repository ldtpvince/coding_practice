# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Solution: DP
# The max amount of money at n-th place is:
# max_amount_n = max(max_amount_n-2 + cur_amount_money_n, max_amount_n-3 + cur_amount_money_n)

def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    if len(nums) == 3:
        return max(nums[0] + nums[2], nums[1])
    
    nums[2] = nums[0] + nums[2]
    for i in range(3, len(nums)):
        nums[i] = max(nums[i] + nums[i-2], nums[i] + nums[i - 3])
        
    return max(nums[len(nums) -1], nums[len(nums) - 2])