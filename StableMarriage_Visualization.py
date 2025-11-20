'''
    Filename: StableMarriage_Visualization.py
    Author: Cydney Miller
    Date Created: 11/19/2025
    Last Updated: 11/19/2025
    Purpose: Create a program that explains what the Stable Marriage Problem
             is with meaningful and educational visualizations.
'''
import os
import matplotlib.pyplot as plt
import numpy as np

def main():

    # Introduce the purpose of the program and what it will accomplish.
    print("\nWelcome to An Explanation of the Stable Marriage Problem!")
    print("\nThis program will briefly describe the Stable Marriage Problem, some of its")
    print("applicaitons, then give a step-by-step visualization for solving such problem.\n")
    os.system('pause')
    print("--------------------------------------------------------------------------------------")

    # Give an overview of the Stable Marriage Problem
    print_overview()

    # FIXME this is just the test. Each step will need to be edited in the future
    print_step1()

def print_overview():
    print("\nOverview:")
    print("The Stable Marriage Problem is concerned with pairing N men and N women, each having")
    print("ranked all members of the opposite sex by preference. The goal is to form marriages")
    print("such that no two individuals would prefer each other over their assigned partners.\n")
    os.system('pause')
    print("\nIt is important to note that we aim to \"...model a methematical problem. We will not,")
    print("for instance, consider the realities of same-sex marriage, that individuals don't ")
    print("necessarily identify as male or female, and that women often propose to men,\" (Austin).\n")
    os.system('pause')
    print("--------------------------------------------------------------------------------------")

def print_step1():
    # --- SETTINGS YOU CAN EDIT --------------------------------------

    men = ["m1", "m2", "m3", "m4"]
    women = ["w1", "w2", "w3", "w4"]

    # List of (row, col) coordinates to color blue.
    # (0,0) is the top-left cell inside the grid (after headers).
    blue_cells = [
        (0, 2),  # m1 - w3
        (1, 3),  # m2 - w4
        (2, 1),  # m3 - w2
        (3, 1),  # m4 - w2
    ]

    # Colors
    header_color = "#f4b942"   # gold
    row_label_color = "#f48fb1"  # pink
    blue_color = "#7f8cff"       # blue
    line_color = "gray"

    # ---------------------------------------------------------------

    # Create 5×5 grid (1 row/col for labels, 4×4 for content)
    fig, ax = plt.subplots(figsize=(6, 6))

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw grid lines
    for x in range(6):
        ax.plot([x, x], [0, 5], color=line_color, linewidth=1)
        ax.plot([0, 5], [x, x], color=line_color, linewidth=1)

    # Color column headers (women)
    for j, w in enumerate(women):
        ax.add_patch(plt.Rectangle((j+1, 4), 1, 1, color=header_color))
        ax.text(j+1.5, 4.5, w, va="center", ha="center", fontsize=12)

    # Color row headers (men)
    for i, m in enumerate(men):
        ax.add_patch(plt.Rectangle((0, 3-i), 1, 1, color=row_label_color))
        ax.text(0.5, 3.5-i, m, va="center", ha="center", fontsize=12)

    # Fill blue cells
    for (i, j) in blue_cells:
        ax.add_patch(plt.Rectangle((j+1, 3-i), 1, 1, color=blue_color))

    # Set axis limits
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.invert_yaxis()

    plt.show()

if __name__ == "__main__":
    main()

