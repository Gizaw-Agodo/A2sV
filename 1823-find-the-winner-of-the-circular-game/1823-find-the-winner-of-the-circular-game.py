class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        mylist = [i for i in range(1,n+1)]
        index = 0
        while len(mylist) > 1 : 
            index = (index + k-1)%len(mylist)
            mylist = mylist[:index] + mylist[index+1:]
            print(mylist)
        return mylist[0]