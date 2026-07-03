# Given an integer array num, return true if any value occurs atleasrt twice in a the list, return false if elements are distinct


nums = [1, 2, 3, 4, 5, 4]
elements = set()


def duplicates(nums, elements):
    for num in nums:
        if num in elements:
            return True
        else:
            elements.add(num)
    return False


print(duplicates(nums, elements))
