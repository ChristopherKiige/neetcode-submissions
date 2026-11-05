class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            frequent[num] = frequent.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in frequent.items():
            buckets[count].append(num)

        final = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                final.append(num)
                if len(final) == k:
                    return final