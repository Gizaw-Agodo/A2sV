# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def getMountain():
            start = 0
            end = n
            while start <= end : 
                mid = start + (end - start)//2
                prev = -1
                next = float('inf')
                if mid -1 >= 0 : 
                    prev = mountain_arr.get(mid - 1)
                if mid + 1 < n:
                    next = mountain_arr.get(mid + 1)
               
                if  prev < mountain_arr.get(mid) > next :
                    return mid
                elif prev < mountain_arr.get(mid) < next :
                    start = mid + 1
                else:
                    end = mid - 1
            
        

        def getElement(start, end, type):
            
            while start <= end : 
                mid = start + (end - start)//2
                element = mountain_arr.get(mid)
                if element == target:
                    return mid
                elif type == "INC":
                    if element > target :
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if element > target :
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1
        
        mount_index = getMountain()
        index1 = getElement(0, mount_index , "INC")
        if index1 == -1:
            return getElement(mount_index ,n-1, 'DEC')

        return index1
    





            
