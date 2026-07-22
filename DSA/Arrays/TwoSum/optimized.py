"""
Problem:
Given an array of integers and a target value,
return the indices of the two numbers whose sum equals the target.

Algorithm:
1. create a dictionary
2. iterate through the array
3. for each number, calculate its complement (target - number)
4. check if complement existes in dictionary
5. if exists, return the indices of the current number and it's complement
6. if not, add the current number  as key and its index as value to the dictionary

"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen : dict[int , int] = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))