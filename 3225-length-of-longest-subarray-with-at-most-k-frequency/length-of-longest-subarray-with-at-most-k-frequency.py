class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency={}
        left=0
        longest_length=0
        for right in range(len(nums)):
            frequency[nums[right]]=frequency.get(nums[right],0)+1
            while frequency[nums[right]]>k:
                frequency[nums[left]]-=1
                left+=1
            longest_length=max(longest_length,right-left+1)
        return longest_length