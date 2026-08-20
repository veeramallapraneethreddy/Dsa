class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        first_array=[nums[0]]
        second_array=[nums[1]]
        for i in range(2,len(nums)):
            if first_array[-1]>second_array[-1]:
                first_array.append(nums[i])
            else:
                second_array.append(nums[i])
        return first_array+second_array