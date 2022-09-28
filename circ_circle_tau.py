#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Sep. 27, 2022
# This program asks the user for the radius in cm
# then calculates and displays circumference AND area of a circle
import math

import constants


def main():
    # input
    print("circumference and area of a circle calculator")
    print("")
    radius = float(input("Enter the radius of the circle (cm): "))

    # process
    circumference = constants.TAU * radius
    area = math.pi * radius**2

    # output
    print("")
    print("circumference = {} cm".format(circumference))
    print("area = {} cm^2".format(area))


if __name__ == "__main__":
    main()
