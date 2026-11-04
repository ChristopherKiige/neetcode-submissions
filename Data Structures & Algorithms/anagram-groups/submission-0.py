class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bins = {}

        for word in strs:
            label = "".join(sorted(word))
            
            if label not in bins:
                bins[label] = []

            bins[label].append(word)

        return list(bins.values())
