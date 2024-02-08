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
           ('Neptune', 4500))


def get_integer_input(message, min_num, max_num):
    """
    Get a valid integer value from the user
    ---
    :param message: user's input
    :param min_num: min integer input value allowed
    :param max_num: max integer input value allowed
    :return user_input
    """

    while True:
        try:
            user_input = int(input(message))

            if min == 0 and max == 0:
                return user_input
            elif min_num <= user_input <= max_num:
                return user_input
            else:
                print(f"\tInvalid Input: Please enter a number between {min_num} and {max_num}.")
                continue

        except ValueError:
            print("\tInvalid Input: Please enter a number.")
            continue


def display_abs_distance(planet1_num, planet2_num):
    """
    Takes in the users two planets numbers and unpacks the tuple. The function then subtracts the
    two numbers from each other using the absolute function. It then displays a message with the
    total distance
    """
    planet1_info = PLANETS[planet1_num - 1]
    planet1_name, planet1_dist = planet1_info

    planet2_info = PLANETS[planet2_num - 1]
    planet2_name, planet2_dist = planet2_info

    dist_between = abs(planet1_dist - planet2_dist)

    print(planet1_name, "and", planet2_name, "are", dist_between, "million miles apart!")


def display_planets_menu():
    """
    Displays the planets menu and how far away from the sun they are.
    """
    # Displays header for the program
    print('=' * MAX_LINE)
    print("Planet's Average Distance From Sun")
    print('=' * MAX_LINE)

    # Displays each planet with their name and distance from the sun and assigns it a menu number
    menu_number = 1
    for planet_name, planet_distance in PLANETS:
        print(f"#{menu_number} {planet_name:<7} = {planet_distance:>4} million miles")
        menu_number += 1

    print('=' * MAX_LINE)


def main():
    """
    First displays the planets menu then asks for two planets then calls display_abs_distance to display how far
    the two planets are from each other. At the end displays the message live long and prosper V.
    """
    display_planets_menu()

    # Gets the first planet menu input number
    while True:
        planet1_num = get_integer_input("Please enter the 1st Planet #", min_num=0, max_num=len(PLANETS))

        # Have 0 end the program
        if planet1_num == 0:
            break

        # Gets the second planet menu input number
        while True:
            planet2_num = get_integer_input("Please enter the 2nd Planet #", min_num=0, max_num=len(PLANETS))

            # Error handling if the planet numbers are the same
            if planet1_num == planet2_num:
                print("Invalid Input: The same planet was entered twice")
            else:
                break

        # Have 0 end the program
        if planet2_num == 0:
            break

        # Calls this function to display distance between the two planets
        display_abs_distance(planet1_num, planet2_num)

        # Closing message before the program loops through again
        input("Press enter to continue...")
        print('=' * MAX_LINE)
        print("Live Long and Prosper V")
        print('=' * MAX_LINE)


if __name__ == "__main__":
    main()
