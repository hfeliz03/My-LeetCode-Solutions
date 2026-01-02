class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        result = {}
        for i, num in enumerate(numsSorted):
            result[num] = result.get(num, i)
        
        output = []
        for num in nums:
            output.append(result.get(num))

        print(nums)
        print(result)
        print(output)
        return output

