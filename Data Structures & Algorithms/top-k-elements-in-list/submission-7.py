class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = nums.count(num)

        sorted_hm = dict(sorted(hm.items(),key= lambda item: item[1] ,reverse=True))

        count = 1
        top_k = []
        for num in sorted_hm:
            if count > k:
                break
            top_k.append(num)
            count += 1

        return top_k