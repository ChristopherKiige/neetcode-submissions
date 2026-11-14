class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))
        count  = 0
        total = 1

        if(len(sorted_list) == 1):
            return 1
        elif(len(sorted_list) == 0):
            return 0

        for i in range(len(sorted_list)):
            if (i == len(sorted_list) - 1):
                break;

            if(sorted_list[i] + 1 == sorted_list[i + 1]):

                if(count == 0):
                    count += 1

                count += 1

                if(total < count):
                    total = count
            else:
                count  = 0

        return total
