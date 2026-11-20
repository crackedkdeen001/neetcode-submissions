class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        
        buckets = [[] for i in range(len(nums))]
        for num, freq in frequency.items():
            # freq -1 to make it 0 indexed
            buckets[freq -1].append(num)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if not bucket:
                continue

            for number in bucket:
                k -= 1
                result.append(number)

            if k == 0:
                break
        
        return result



        """
        problem: from an array of integers, return the top k frequent elements
        input: an array of integers
        output: a list of the top k frequent elements

        brute force approach:
        use a hashmap to get the number of occurences of each element in the hashmap
        sort the hashmap based on the occurences, and return the list of top k elements

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            count[num] = 1

        sorted_count = Sort(count, count.items()[1])
        sorted_nums = list(sorted_count.keys())
        return sorted_nums[:k]

        optimal 
        we use bucket sort to group each number by how often it appears in the array.
        array of arrays as our buckets.
        We first create a hashmap to get the frequency of each number in the array
        we then create a bucket with an empty array at each index, with each index representing the number of times an element appeared in the og array
        Then, we traverse the hashmap and using the frequency as an index, we add each number to it's corresponding bucket based on the it's frequency

        we then initialize our result an array to the top k elements.
        We then traverse our bucket from the n to 1 to make getting the top k easier.
        we add the each element to the result array until we've got the top k elements, and we return k
        """