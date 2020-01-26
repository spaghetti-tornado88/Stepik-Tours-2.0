from flask import Flask
from data import *

print(list(tours))
tours_items_list = list(tours.items())
print(sorted(tours_items_list, reverse=True, key=lambda x: x[1].get('price')))

for tour_id, tour in sorted(tours_items_list, reverse=True, key=lambda x: x[1].get('price')):
    print(tour_id, tour)


