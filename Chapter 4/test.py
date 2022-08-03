from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        for i in range(len(nums)-1):
            need = target - nums[i]
            print(need,  target , nums[i] ,'left:', nums[i:])

            if need in nums[i+1:]:

                # find index
                j = min([e for e, val in enumerate(nums) if val == need and e != i ])
                print('j', j)
                result = [i , j]
                break
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [2,7,11,15]
    target = 9

    nums = [3,2,4]
    target = 6

    nums = [3,3,3]
    target = 6

    result = s.twoSum(nums=nums, target=target)
    print(result)