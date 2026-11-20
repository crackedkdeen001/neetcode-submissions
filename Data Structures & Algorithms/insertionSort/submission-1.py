# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        if not pairs:
            return res

        # use a copy because pairs is a reference
        # and since insertion sort is in place
        # the original array get modified
        res.append(pairs[:])
        for i in range(1, len(pairs)):
            pair = pairs[i] 

            j = i - 1
            # finding where the key stays in the array
            while j > -1 and pairs[j].key > pair.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = pair
            res.append(pairs[:])

        return res
                
            
