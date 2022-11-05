class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dic = defaultdict(int)
        start = 0
        maximum = 0
        for i in range(len(answerKey)):
            dic[answerKey[i]]+=1
            if i-start +1 - max(dic.values()) <= k:
                maximum = max(maximum,i-start+1)
            while i-start +1 - max(dic.values()) > k:
                dic[answerKey[start]]-=1
                start +=1
        return maximum
                