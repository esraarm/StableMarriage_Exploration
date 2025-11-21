'''
    Filename: main.py
    Author: Cydney Miller
    Date Created: 11/19/2025
    Last Updated: 11/19/2025
    Purpose: Create a program that explains what the Stable Marriage Problem
             is with meaningful and educational visualizations.
'''
import os
import matplotlib.pyplot as plt
import numpy as np
from graph import GraphCell
from colors import bcolors
import json

def main():
    # open and load in graph.json data
    with open("Stable_Marriage_Visualization/graphs.json", "r") as jsonFile:
        data = json.load(jsonFile)

    # Introduce the purpose of the program and what it will accomplish.
    print("\nWelcome to An Explanation of the Stable Marriage Problem!")
    print("\nThis program will briefly describe the Stable Marriage Problem, some of its")
    print("applicaitons, then give a step-by-step visualization for solving such problem.\n")
    os.system('pause')
    print("--------------------------------------------------------------------------------------")

    # Give an overview of the Stable Marriage Problem
    print_overview()

    # Print the representative graphs and descriptions
    print_graphs(data)

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

def print_graphs(data):
    for graph_name, graph_data in data["graphs"].items():
        print(f"{graph_name}:")
        cell_obj = GraphCell()
        cell_obj.print_row_one()
        # Define the grid order (adjust as needed for your data)
        men = ["m1", "m2", "m3", "m4"]
        row_keys = [["a1", "a2", "a3", "a4"], ["b1", "b2", "b3", "b4"], ["c1", "c2", "c3", "c4"], ["d1", "d2", "d3", "d4"]]

        for row_idx, row in enumerate(row_keys):
            cell_lines = []
            # Add the man label as a cell (can be styled as you wish)
            cell_lines.append(GraphCell().get_male_cell_lines(men[row_idx]))
            for cell in row:
                cell_data = graph_data.get(cell, {})
                proposed = cell_data.get("proposed")
                engaged = cell_data.get("engaged")
                cell_obj = GraphCell(proposed, engaged)
                cell_lines.append(cell_obj.get_cell_lines())
            for i in range(4):  # 4 lines per cell
                print("  ".join(cell[i] for cell in cell_lines))
        print_description(graph_name)
        os.system('pause')
        print()  # Blank line between graphs

def print_description(graph_name):
    if graph_name == "Step 1A":
        print("\nEach man proposes to the woman he most prefers:")
        print("\tm1 proposes to w1")
        print("\tm2 proposes to w1")
        print("\tm3 proposes to w2")
        print("\tm4 proposes to w4\n")
    elif graph_name == "Step 1B":
        print("\nNotice that w1 receives proposals from m1 and m2. She")
        print("chooses the proposal from m1 since she prefers m1 to m2.\n")
    elif graph_name == "Step 2A":
        print("\nSince m2 has been rejected by w1, he proposes to his second choice, w4.\n")
    elif graph_name == "Step 2B":
        print("\nNow w4 has proposals from m2 and m4 of which she chooses the one from m2.\n") 
    elif graph_name == "Step 3A":
        print("\nm4 proposes to w2...\n") 
    elif graph_name == "Step 3B":
        print("\nwho accepts the proposal and rejects m3.\n") 
    elif graph_name == "Step 4A":
        print("\nm3 proposes to w1...\n") 
    elif graph_name == "Step 4B":
        print("\nwho accepts the proposal and rejects m1.\n")  
    elif graph_name == "Step 5A":
        print("\nm1 proposes to w2...\n")  
    elif graph_name == "Step 5B":
        print("\nwho rejects him because she prefers her current partner, m4.\n")  
    elif graph_name == "Step 6A":
        print("\nm1 proposes to w3...\n")  
    elif graph_name == "Step 6B":
        print("\nwho accepts his proposal, which is our final marriage.\n")   
    else:
        print("\nWe haven't gotten there yet!\n")
        

if __name__ == "__main__":
    main()

