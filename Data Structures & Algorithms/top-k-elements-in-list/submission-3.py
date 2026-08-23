from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # # manual counting (nlogn)
        # hmap = {}

        # for i in range(len(nums)):

        #     if (nums[i] in hmap):
        #         hmap[nums[i]] += 1
        #     else:
        #         hmap[nums[i]] = 1

        
        # sorted_hmap = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
        # res = []

        # for i in range(k):
        #     res.append(sorted_hmap[i][0])

        # return res

        # Bucket Sort (O(N) or O(nlogk))
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []

        for count in range(len(buckets) - 1, -1, -1):

            for num in buckets[count]:
                res.append(num)

                if len(res) == k:

                    return res