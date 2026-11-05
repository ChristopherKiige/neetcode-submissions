class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        final = []

        if len(nums) == 0:
            return nums

        for num in nums:
            frequent[num] = frequent.get(num, 0) + 1
        
        result  = sorted(frequent, key=lambda num: frequent[num])

        while k > 0:
            final.append(result[len(result) - k])
            k = k - 1
        
        return final
            
        

            