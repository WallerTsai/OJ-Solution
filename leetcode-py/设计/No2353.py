from collections import defaultdict
from typing import List
from heapq import heapify, heappop, heappush,heapreplace

# class FoodRatings:

#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.foods_map = {}
#         self.cuisine_map = defaultdict(list)
#         for food,cuisine,rating in zip(foods,cuisines,ratings):
#             self.foods_map[food] = [rating,cuisine]
#             heappush(self.cuisine_map[cuisine],(-rating,food))

#     def changeRating(self, food: str, newRating: int) -> None:
#         food_map = self.foods_map[food]
#         heapreplace(self.cuisine_map[food_map[1]])

#     def highestRated(self, cuisine: str) -> str:
        
class FoodRatings:
    # 懒删除堆
    # 灵神
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            self.cuisine_map[cuisine].append((-rating, food))
        # 这样可以保证初始化是线性复杂度
        for h in self.cuisine_map.values():
            heapify(h)

    def changeRating(self, food: str, newRating: int) -> None:
        p = self.food_map[food]
        # 直接添加新数据，后面 highestRated 再删除旧的
        heappush(self.cuisine_map[p[1]], (-newRating, food))
        p[0] = newRating

    def highestRated(self, cuisine: str) -> str:
        h = self.cuisine_map[cuisine]
        # 堆顶的食物评分不等于其实际值
        while -h[0][0] != self.food_map[h[0][1]][0]:
            heappop(h)
        return h[0][1]


class FoodRatings:
    # 灵神
    # 有序列表
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)  # sortedcontainers
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            # 取负号，保证 rating 相同时，字典序更小的 food 排在前面
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating, food))  # 移除旧数据
        sl.add((-newRating, food))  # 添加新数据
        self.food_map[food][0] = newRating  # 更新 food 的 rating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]
    
class FoodRatings:
    # 懒删除堆
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            heappush(self.cuisine_map[cuisine],(-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        p = self.food_map[food]
        heappush(self.cuisine_map[p[1]], (-newRating, food))
        p[0] = newRating

    def highestRated(self, cuisine: str) -> str:
        h = self.cuisine_map[cuisine]
        while -h[0][0] != self.food_map[h[0][1]][0]:
            heappop(h)
        return h[0][1]