def twoSum(self, nums, target):
    dict9 = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict9:
            return [dict9[complement], i]
        dict9[nums[i]] = i