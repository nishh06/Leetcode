 def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(set(nums))
        c=0
        for i in nums:
            if i > 0 :
                c +=1
                if i != c:
                    return c
        return c+1

nums = [1,2,4]
res = firstMissingPositive(nums)
print(res)