# You are given a list of numbers and a target total.
# You need to find two numbers in that list that add up exactly to the target,
# and return their index positions.


nums = [2, 7, 11, 15]
target = 9
store = {}
for i, num in enumerate(nums):
    if (target - num) in nums:
        store[num] = i
    else:
        continue

if store is not None:
    print(list(store.keys()))
