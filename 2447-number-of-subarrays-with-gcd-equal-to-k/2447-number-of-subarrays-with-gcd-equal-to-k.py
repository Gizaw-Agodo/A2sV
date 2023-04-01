class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1%num2)
        
        answer = 0
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i,len(nums)):
                curr_gcd = gcd(max(nums[j],curr_gcd),min(nums[j],curr_gcd))
                if curr_gcd == k:
                    answer += 1
                elif curr_gcd < k:
                    break
        return answer