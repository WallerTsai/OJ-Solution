from collections import defaultdict
from typing import List
from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.shop_movie_to_price = dict()
        self.unrented_movie_to_price_shop = defaultdict(SortedList)
        self.rented_movies = SortedList()

        for shop, movie, price in entries:
            self.shop_movie_to_price[(shop,movie)] = price
            self.unrented_movie_to_price_shop[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        return[shop for _, shop in self.unrented_movie_to_price_shop[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        self.unrented_movie_to_price_shop[movie].remove((price, shop))
        self.rented_movies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        self.rented_movies.remove((price, shop, movie))
        self.unrented_movie_to_price_shop[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented_movies[:5]]


