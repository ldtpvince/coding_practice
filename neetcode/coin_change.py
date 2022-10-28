# Question: https://leetcode.com/problems/coin-change/
# Solution: DP

# Let assume that we want to know the fewest number of coins for r  (where 0 <= r < amount) so:
#     num_for_r = min([num_for_(r - c_i) + 1 for every c_i coin from the given pool])
# Base case: num_for_c_i = 1