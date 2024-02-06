#!/user.bin.env python3

"""
Usage: Planet_Distances.py
User inputs two different planets to calculate the distance between them.

GitHub: https://github.com/caleb-jenkinson15/Planet_Distances
"""

# metadata (RY- Currently written as in set up video, will be altered to include second programmer)
__author__ = 'Rivar Yoder, Caleb Jenkinson'
__date__ = '2023/07/02'
__email__ = 'alyode01@wsc.edu, cajenk01@wsc.edu'
__version__ = '0.0.1'

MAX_LINE = 60

PLANETS = (('Mercury', 57),
           ('Venus', 108),
           ('Earth', 150),
           ('Mars', 228),
           ('Jupiter', 779),
           ('Saturn', 1430),
           ('Uranus', 2880),
           ('Neptune', 4500)
)


def display_planets_menu():
    print('=' * MAX_LINE)
    print("Planet's Average Distance From Sun")
    print('=' * MAX_LINE)

    menu_number = 1
    for planet_name, planet_distance in PLANETS:
        print(f"#{menu_number} {planet_name:<7} = {planet_distance:>4} million miles")
        menu_number += 1

    print('=' * MAX_LINE)


display_planets_menu()

