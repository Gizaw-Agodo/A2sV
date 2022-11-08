class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        answer = []
        restaurants.sort(key =lambda x :(-x[1],-x[0]))
        for i in range(len(restaurants)):
            i,r,v,p,d = restaurants[i]
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                answer.append(i)
        return answer
