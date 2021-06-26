def twoSum(nums, target):
    saw = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in saw.keys():
            return [saw[nums[i]], i]
        else:
            saw[diff]=i

li = [12, 4, 6, 7, 3, 10]
print(twoSum(li, 10))

