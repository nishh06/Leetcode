def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    hashMap = {}
    for num in nums:
        if num in hashMap:
            return num
        else:
            hashMap[num] = 1
nums = [1,3,4,2,2]
res = findDuplicates(nums)
print(res)
