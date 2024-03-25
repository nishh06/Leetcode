def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    duplicates = []
    hashMap = {}
    for num in nums:
        if num in hashMap:
            duplicates.append(num)
        else:
            hashMap[num] = 1
    return duplicates

nums = [4, 3, 2, 7, 8, 2, 3, 1]
res = findDuplicates(nums)
print(res)
