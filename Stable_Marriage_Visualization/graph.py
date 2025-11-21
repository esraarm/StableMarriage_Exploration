'''
    Filename: graph.py
    Author: Cydney Miller
    Date Created: 11/20/2025
    Date Updated: 11/20/2025
    Purpose: Class to create representative graphs in the terminal.
'''
from colors import bcolors

class GraphCell():
    # Constructor
    def __init__(self, proposed = "False", engaged = "False"):
        self.__proposed = proposed
        self.__engaged = engaged

    # prints the header row of women for each graph    
    def print_row_one(self):
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}| w1 |  | w2 |  | w3 |  | w4 |{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}|    |  |    |  |    |  |    |{bcolors.RESET}")
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")

    # Format the male cell similarly to the women cells in print_row_one
    def get_male_cell_lines(self, man_label):
        return [
            f"{bcolors.MEN}------{bcolors.RESET}",
            f"{bcolors.MEN}| {man_label} |{bcolors.RESET}",
            f"{bcolors.MEN}|    |{bcolors.RESET}",
            f"{bcolors.MEN}------{bcolors.RESET}"
        ]

    # depending on which row we are on, print the correct man
    def print_male_cell(self, man):
        if man == 1:
            print("------")
            print("| m1 |")
            print("|    |")
            print("------")
        elif man == 2:
            print("------")
            print("| m2 |")
            print("|    |")
            print("------")
        elif man == 3:
            print("------")
            print("| m3 |")
            print("|    |")
            print("------")
        else:
            print("------")
            print("| m4 |")
            print("|    |")
            print("------")

    # rule for how each cell should be printed depending on its values for 'proposed' and 'engaged'
    def get_cell_lines(self):
        if self.__proposed == "True":
            return [
                f"{bcolors.PROPOSED}------{bcolors.RESET}",
                f"{bcolors.PROPOSED}|////|{bcolors.RESET}",
                f"{bcolors.PROPOSED}|////|{bcolors.RESET}",
                f"{bcolors.PROPOSED}------{bcolors.RESET}"
            ]
        elif self.__engaged == "True":
            return [
                f"{bcolors.ENGAGED}------{bcolors.RESET}",
                f"{bcolors.ENGAGED}|////|{bcolors.RESET}",
                f"{bcolors.ENGAGED}|////|{bcolors.RESET}",
                f"{bcolors.ENGAGED}------{bcolors.RESET}"
            ]
        else:
            return [
                "------",
                "|    |",
                "|    |",
                "------"
            ]