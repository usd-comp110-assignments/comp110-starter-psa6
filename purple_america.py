"""
Module: purple_america

Program for visualizing election results in interesting ways.

Author: <INSERT YOUR FULL NAME AND USD EMAIL HERE>
"""

import turtle

def draw_subregion(my_turtle, polygon_points):
    """Draws a polygonal subregion.

    Args:
        my_turtle: The turtle that will do the drawing.
        polygon_points: List of tuples of the coordinates of the polygonal region.
    """

    pass  # To Do: replace this line with your implemenation


def draw_filled_subregion(my_turtle, polygon_points, pen_color,fill_color):
    """Replace this with a docstring comment with the correct format."""

    pass  # To Do: replace this line with your implemenation


def read_subregion(geo_file):
    """Replace this with a docstring comment with the correct format."""

    return None, None  # To Do: eplace this line with your implemenation

def calculate_colors(style, votes):
    """Replace this with a dcostring comment with the correct format."""

    return None, None # To Do: replace this line with your implemenation

def get_election_results(election_filename):
    """Replace this with a docstring comment with the correct format."""

    return None  # To Do: replace this line with your implemenation

def draw_map(geo_filename, election_results, style):
    """Replace this with a docstring comment with the correct format."""

    pass  # To Do: replace this line with your implemenation

def main():
    """Program that draws an electoral map based on geographic and election data."""

    geo_filename = input("Enter the name of the geography file: ")
    election_filename = input("Enter the name of the election data file: ")

    valid_input = False
    while not valid_input:
        prompt_string = "What style of map would you like?\n"
        prompt_string += "Enter 1 for black & white.\n"
        prompt_string += "Enter 2 for red & blue.\n"
        prompt_string += "Enter 3 for purple.\n"
        style_selection = input(prompt_string)
        if style_selection == "1":
            valid_input = True
            style = "black-white"
        elif style_selection == "2":
            valid_input = True
            style = "red-blue"
        elif style_selection == "3":
            valid_input = True
            style = "purple"
        else:
            print("Invalid selection!")


    # To Do: Write your code to complete this function below here and then remove this comment.


# WARNING: Do NOT modify anything below this point.

if __name__ == "__main__":
    main()
