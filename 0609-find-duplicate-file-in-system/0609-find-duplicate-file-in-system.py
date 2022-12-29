class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dic = defaultdict (int)
        answer_dic = defaultdict(list)
        answer = []
        for path in paths:
            files = path.split()
            for i in range(1,len(files)):
                splited =  files[i].split("(")
                content_dic[splited[1][:-1]] +=1
       
        for path in paths:
            files = path.split()
            for i in range(1,len(files)):
                splited =  files[i].split("(")
                if content_dic[splited[1][:-1]] >1 :
                    answer_dic[splited[1][:-1]].append(files[0]+"/"+splited[0])
        for key  in answer_dic:
            answer.append(answer_dic[key])
        return answer
            