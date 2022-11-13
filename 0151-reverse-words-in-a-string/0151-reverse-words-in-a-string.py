class Solution:
    def reverseWords(self, s: str) -> str:
     
        words= s.split(" ")
        start,end = 0,len(words)-1
        while start < end:
            if words[start]=="":
                start+=1
            if words[end] == "":
                end-=1
            if words[end]!="" and words[start]!="":
                words[start],words[end] = words[end],words[start]
                end-=1
                start+=1
        answer = []
        for word in words :
            if word != "":
                answer.append(word)
        return " ".join(answer)
            
        
        