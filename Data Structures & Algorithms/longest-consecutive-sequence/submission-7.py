class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put every number in a set.
        # This removes duplicates AND lets us check "is X in here?" instantly (O(1)),
        # instead of scanning the whole list each time (O(n)).
        num_set = set(nums)

        # Longest streak found so far.
        # Starts at 0 so an empty list correctly returns 0.
        longest = 0

        # Loop over the set (not nums) so duplicates are only looked at once.
        for num in num_set:

            # KEY IDEA: only start counting if num is the START of a streak.
            # If num - 1 exists, num is in the middle of someone else's streak,
            # so counting from here would just repeat work. Skip it.
            if num - 1 not in num_set:

                # num is a streak start. A single number is a streak of length 1.
                length = 1

                # Keep checking if the next number exists.
                # e.g. start at 2: is 3 here? is 4? is 5? ... until one is missing.
                while num + length in num_set:
                    length += 1

                # Keep the biggest streak we've seen.
                longest = max(longest, length)

        return longest