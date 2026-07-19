# Two Sum

## Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Brute Force Approach

## Algorithm
1. Iterate each element in the array
2. Compare it with all remaining numbers
3. If the sum equals the target, return the indices
4. If no pair exists, return an empty list.

## Time Complexity
Outer Loop : O(n)
Inner Loop : O(n)
Total : O(n^2)

## Space Complexity
O(1)
No extra data structures are used.

## Advantages

## Disadvantages

## Can it be optimized?

## Real-world Learning
Question 1: Why did you use range(len(nums)) instead of for number in nums
Ans: 
1. Because we need an indices, not just the values.
2. for number in nums gives only values.
3. range(len(nums)) access both the index and the value (nums[i])

Question 2: Why does the inner loop start from i + 1?
Ans:
To avoid:
* Comapring an element with itself.
* Checking the same pair twice.
* without i+1, we would compare (1,2) and later (2,1) which is redundant.

Question 3: Why did you write return [] instead of return None?
Ans:
* Because the function's return type is expected to be List[int] returning [] means
"No valid indices were found"
* Returning "None" would require every caller to explicitly check for None, and it no longer matches the expected return type. 
