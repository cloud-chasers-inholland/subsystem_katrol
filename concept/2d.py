import math


# Define dimensions for 3d space. Dimensions are in milimeters.
BASE_LENGTH = 700
BASE_WIDTH = 500


# Determine positions of pylons
P_1 = [0, 0]  # Bottom left
P_2 = [BASE_LENGTH, 0]  # Bottom right
P_3 = [0, BASE_WIDTH]  # Top left
P_4 = [BASE_LENGTH, BASE_WIDTH]  # Top right


# Pythagoras to get length from pylon
def distance_location_pylon(loc, p_loc):
    lenght = math.sqrt((p_loc[0] - loc[0]) ** 2 + (p_loc[1] - loc[1]) ** 2)
    return lenght


# Get input and parse into right form
def input_loc():
    txt = input("Give desired location in form x,y")
    loc = [float(x) for x in txt.split(",")]
    return loc


def main():
    location = input_loc()
    print(distance_location_pylon(location, P_1))
    print(distance_location_pylon(location, P_2))
    print(distance_location_pylon(location, P_3))
    print(distance_location_pylon(location, P_4))


if __name__ == "__main__":
    main()
