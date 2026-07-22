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

## Can it be optimized?
Yes. We can optimize the solution using a HashMap (Python dictionary) to reduce the time complexity from O(n²) to O(n).

## Algorithm
1. Create the empty dictionary
2. Iterate through the array
3. For each number, compute the complement ( target - number )
4. Check whether the complement already exists in the HashMap.
5. If found, return the stored index and the current index.
6. Otherwise, store the current number as the key and its index as the value.

## Why HashMap?

The HashMap stores previously processed numbers as keys and their indices as values.

For every current number:

1. Calculate the complement.
2. Check whether the complement already exists in the HashMap.
3. If found, return the indices.
4. Otherwise, store the current number.

This avoids searching the array repeatedly and reduces the time complexity from O(n²) to O(n).

## Real-world Learning
### Question 1: Why did you use range(len(nums)) instead of for number in nums
Answer: 
1. Because we need an indices, not just the values.
2. for number in nums gives only values.
3. range(len(nums)) only gives the index. access the value using (nums[i])
4. In Python, enumerate(nums) is preferred because it directly provides both the index and the value.

### Question 2: Why does the inner loop start from i + 1?
Answer:
To avoid:
* Compring an element with itself.
* Checking the same pair twice.
* without i+1, we would compare (1,2) and later (2,1) which is redundant.

### Question 3: Why did you write return [] instead of return None?
Answer:
* Because the function's return type is expected to be List[int] returning [] means
"No valid indices were found"
* Returning "None" would require every caller to explicitly check for None, and it no longer matches the expected return type. 

### Question 4: Why is the number stored as the key instead of the index?
Answer:
1. The algorithm searches for the complement (a number), not an index.
2. HashMap lookups are performed using keys.
3. Therefore, the number must be the key and the index must be the value.
4. If the index were the key, we'd need to search all values, making the lookup O(n) instead of O(1).

## Key Takeaways

- HashMap provides approximately O(1) average lookup time.
- Store previously processed numbers as keys and their indices as values.
- The algorithm checks whether the current number's complement has already been seen.
- HashMap trades extra memory (O(n)) for better performance (O(n) time).
- enumerate() is a Pythonic way to iterate through both index and value.