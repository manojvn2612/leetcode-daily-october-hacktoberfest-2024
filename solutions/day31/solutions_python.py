class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        left,right = float("inf"),float("-inf")
        for i in range(len(nums)):
            left = min(left,nums[i][0])
            right = max(right,nums[i][0])
            heapq.heappush(min_heap,(nums[i][0],i,0)) #element from each list to keep track of and i for list index and 0 for initial element
        ans = [left,right]
        while True:
            n, i, idx = heapq.heappop(min_heap)
            if idx + 1 == len(nums[i]):
                break
            next_elem = nums[i][idx + 1]
            heapq.heappush(min_heap, (next_elem, i, idx + 1))
            right = max(right, next_elem)
            left = min_heap[0][0]
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
        return ans
