class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        visited = set((nums1[0],nums2[0]))
        heap = [[nums1[0] + nums2[0],0,0]]
        answer = []
        
        while k > 0 and heap:
            currSum, i, j = heappop(heap)
        
            answer.append([nums1[i],nums2[j]])
            k -= 1
            if i < len(nums1) - 1 :
                candidate1 = (i+1,j)
                if candidate1 not in visited:
                    visited.add(candidate1)
                    heappush(heap, [nums1[i + 1] + nums2[j],i+1, j])
            
            if j < len(nums2) - 1:
                candidate2 = (i, j)
                if candidate2 not in visited:
                    heappush(heap, [nums1[i] + nums2[j+1],i, j + 1])
            
            
        return answer
            
        
        