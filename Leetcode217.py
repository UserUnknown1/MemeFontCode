# Given an integer array num, return true if any value occurs atleasrt twice in a the list, return false if elements are distinct


nums = [1, 2, 3, 4, 5, 89]
elements = set(nums)


def duplicates(nums: list, dupe: set):
    if len(nums) is not len(elements):
        return True
    else:
        return False


print(duplicates(nums, elements))
