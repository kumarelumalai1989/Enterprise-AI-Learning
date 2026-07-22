class Solution:
  
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type: target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
solution = Solution()
nums = list(map(int, input("Enter the list of numbers separated by space: ").split()))
target = int(input("Enter the target number: "))

result = solution.twoSum(nums, target)
if result:
   print("\nResult:")
   print("-" * 20)
   print(f"First index: {result[0]}")
   print (f"Second index: {result[1]}")

   print(f"First number: {nums[result[0]]}")
   print(f"Second number: {nums[result[1]]}")
else:
    print("No two sum solution found.")