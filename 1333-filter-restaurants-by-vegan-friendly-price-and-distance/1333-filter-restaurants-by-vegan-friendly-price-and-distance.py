class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        pricei = maxPrice
        disti = maxDistance
        filtered = []
        answer = []
        if veganFriendly == 1:
            for i in range(len(restaurants)):
                id,rating,vegan,price,dis = restaurants[i]
                if vegan == 1  and price <= pricei and dis <= disti:
                    filtered.append(restaurants[i])
            filtered.sort(key= lambda x : (-x[1],-x[0]))
            for i in range(len(filtered)):
                answer.append(filtered[i][0])
            return answer
        else:
            for i in range(len(restaurants)):
                id,rating,vegan,price,dis = restaurants[i]
                if  price <= pricei and dis <= disti:
                    filtered.append(restaurants[i])
            filtered.sort(key= lambda x : (-x[1],-x[0]))
            
            for i in range(len(filtered)):
                answer.append(filtered[i][0])
            return answer