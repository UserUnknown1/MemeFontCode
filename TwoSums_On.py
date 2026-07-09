# You are given a list of numbers and a target total.
# You need to find two numbers in that list that add up exactly to the target,
# and return their index positions.


nums = [2, 7, 11, 15]
target = 9
store = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in store:
        print(store[complement], i)
        break
    store[num] = i
