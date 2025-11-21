'''
    Filename: graph.py
    Author: Cydney Miller
    Date Created: 11/20/2025
    Date Updated: 11/20/2025
    Purpose: Class to create representative graphs in the terminal.
'''
from colors import bcolors

class GraphCell():
    # TODO: rethink the structure of my graph and in turn change the contructor
    def __init__(self, proposed = "False", engaged = "False"):
        self.__proposed = proposed
        self.__engaged = engaged

    def get_proposed(self):
        return self.__proposed
    
    def get_engaged(self):
        return self.__engaged

    
    def print_row_one(self):
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}| w1 |  | w2 |  | w3 |  | w4 |{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}|    |  |    |  |    |  |    |{bcolors.RESET}")
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")
    
    def print_cell(self):
        if self.__proposed == "True":
            print(f"{bcolors.PROPOSED}------{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}|////|{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}|////|{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}------{bcolors.RESET}")
        elif self.__engaged == "True":
            print(f"{bcolors.ENGAGED}------{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}|////|{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}|////|{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}------{bcolors.RESET}")
        else:
            print("------")
            print("|    |")
            print("|    |")
            print("------")

    def get_male_cell_lines(self, man_label):
        # Format the male cell similarly to the women cells in print_row_one
        return [
            f"{bcolors.MEN}------{bcolors.RESET}",
            f"{bcolors.MEN}| {man_label} |{bcolors.RESET}",
            f"{bcolors.MEN}|    |{bcolors.RESET}",
            f"{bcolors.MEN}------{bcolors.RESET}"
        ]

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