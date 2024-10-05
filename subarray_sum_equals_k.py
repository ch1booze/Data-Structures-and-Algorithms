# LeetCode 560: Subarray Sum Equals K

def subarraySum(self, nums, k):
    kSumCount = 0
    window = 1
    arrayLength = len(nums) + 1
    nums = sorted(nums)

    while True:
        for i in range(0, arrayLength-window):
            if sum(nums[i:i+window]) == k:
                kSumCount += 1

        window += 1
        if window >= arrayLength:
            break

    return kSumCount

print(subarraySum("", [1, 1, 1], 2))
