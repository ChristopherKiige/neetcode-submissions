class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[r] + numbers[l]
            if(cur_sum > target):
                r -= 1
            elif(cur_sum < target):
                l += 1
            elif(cur_sum == target):
                return [l+1,r+1]
        return []