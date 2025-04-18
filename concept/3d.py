import math


# Define dimensions for 3d space. Dimensions are in milimeters.
BASE_LENGTH = 700
BASE_WIDTH = 500
BASE_HEIGTH = 500


# Determine positions of attachement from pylon. Every corner and max height of working space
P_1 = [0, 0, BASE_HEIGTH]  # Bottom left
P_2 = [BASE_LENGTH, 0, BASE_HEIGTH]  # Bottom right
P_3 = [0, BASE_WIDTH, BASE_HEIGTH]  # Top left
P_4 = [BASE_LENGTH, BASE_WIDTH, BASE_HEIGTH]  # Top right


# Pythagoras to get length between position and pylon
def distance_location_pylon(loc, p_loc):
    lenght = math.sqrt(
        (p_loc[0] - loc[0]) ** 2 + (p_loc[1] - loc[1]) ** 2 + (p_loc[2] - loc[2]) ** 2
    )
    return lenght


# Get input and parse into right form
def input_loc():
    txt = input("Give desired location in form x,y,z")
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
