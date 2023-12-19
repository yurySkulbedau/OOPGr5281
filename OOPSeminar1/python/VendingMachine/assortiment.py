from Domain.bottle import Bottle
from Domain.product import Product
from Domain.hotdrink import HotDrink
from typing import List

assort: List[Product] = [
        Product(100, 1, "Lays"),
        Product(50, 2, "Cola"),
        Bottle(150, 3, "Mineral Water", 101, 1.5),
        HotDrink(120, 4, "Coffee", 102, 80),
        HotDrink(100, 5, "Tea", 103, 100)
    ]