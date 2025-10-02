nums = list(map(int, input().split()))
nums.sort()
print(nums)
nums.reverse()
print(nums)
for i in range(len(nums)-2):
    c = nums[i]
    a = nums[i + 1]
    b = nums[i + 2]
    if c < a + b:
        print(a + b + c)
        break
print(0)