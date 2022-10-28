# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Solutions: DP
# The same with House Robber one but with a little twist
# Because the the first house and the last one cant co-exist in the final sum
# So: max_money = max(house_robber_one_sol(1, last), house_robber_one_sol(0, last -1))


def helper(self, nums, i, j):
    ma = -1
    a, b, c = nums[i], max(nums[i], nums[i + 1]), -1
    for k in range(i + 2, j + 1):
        c = nums[k]
        c = max(a + c, b)
        a, b = b, c
        ma = max(c, ma)
        
    return ma
    
def rob(self, nums: List[int]) -> int:
    l = len(nums)
    if l == 1:
        return nums[0]
    
    if l == 2:
        return max(nums[0], nums[1])
    
    if l == 3:
        return max(nums[0], max(nums[1], nums[2]))
    
    ma = max(self.helper(nums, 1, l-1), self.helper(nums, 0, l-2))
    
    return ma