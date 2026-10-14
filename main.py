from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    dict = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in dict:
            return [dict[complement], i]
        dict[n] = i

    return []
