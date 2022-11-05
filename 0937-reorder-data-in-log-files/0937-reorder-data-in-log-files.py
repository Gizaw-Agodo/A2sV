class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        for i in range(len(logs)):
            splited = logs[i].split(" ")
            if not(splited[1].isdigit()):
                answer.append([splited[0],splited[1:],i])
        
        answer.sort(key = lambda x :(x[1],x[0]))
        for i in range(len(answer)):
            identifer,_ , index = answer[i]
            answer[i] = logs[index]
        for i in range(len(logs)):
            splited = logs[i].split(" ")
            if splited[1].isdigit():
                answer.append(logs[i])
        return answer