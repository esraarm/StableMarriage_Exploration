'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Filename: main.py
    Author: Cydney Miller
    Date Created: 11/19/2025
    Last Updated: 11/19/2025
    Purpose: Create a program that explains what the Stable Marriage Problem
             is with meaningful and educational visualizations.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
    print("---------------------------------------------------------------------------------------------")

    # Give an overview of the Stable Marriage Problem
    print_overview()
    os.system('pause')
    print("---------------------------------------------------------------------------------------------")


    # Discuss some applications of this problem
    print_applications()
    os.system('pause')
    print("---------------------------------------------------------------------------------------------")


    # Begin visualization section
    print("\nWe will now demonstrate an example of solving the Stable Marriage Problem using the")
    print("most commonly implemented solving method, the Gale Shapley Algorithm.\n")
    os.system('pause')

    # Print preference lists
    print("\nFirst, we will need to define the preference lists for our demonstration.")
    print_preference_lists()
    os.system('pause')
    print("---------------------------------------------------------------------------------------------")

    # Print the representative graphs and descriptions
    print_graphs(data)
    print("---------------------------------------------------------------------------------------------")

    # Print demonstration conclusion
    print_conclusion()
    print("---------------------------------------------------------------------------------------------")

    # Print sources for program
    print_sources()
    print("---------------------------------------------------------------------------------------------\n")



def print_overview():
    print("\nOverview:\n")
    print("The Stable Marriage Problem is concerned with pairing N men and N women, each having")
    print("ranked all members of the opposite sex by preference. The goal is to form marriages")
    print("such that no two individuals would prefer each other over their assigned partners.\n")
    os.system('pause')
    print("\nIt is important to note that we aim to \"...model a mathematical problem. We will not,")
    print("for instance, consider the realities of same-sex marriage, that individuals don't ")
    print("necessarily identify as male or female, and that women often propose to men,\" (Austin).\n")

def print_applications():
    print("\nApplications:\n")
    print("- Medical Student Assignments: Assigning graduating medical students to their first")
    print("  hospital appointments based on their preferences and the preferences of the hospital.")
    print("\n- Content Delivery Networks: Matching users to servers in a large distributed")
    print("  internet service to ensure faster response times and optimal performance.")
    print("\n- Resource Allocation: Matching tasks or resources to agents based on their")
    print("  preferences or priorities in scheduling and resource allocation problems.\n")

def print_preference_lists():
    print("\nMen's Preferences:")
    print(f"\t{bcolors.MEN}m1{bcolors.RESET}: {{{bcolors.WOMEN}w1{bcolors.RESET}, {bcolors.WOMEN}w2{bcolors.RESET}, {bcolors.WOMEN}w3{bcolors.RESET}, {bcolors.WOMEN}w4{bcolors.RESET}}}")
    print(f"\t{bcolors.MEN}m2{bcolors.RESET}: {{{bcolors.WOMEN}w1{bcolors.RESET}, {bcolors.WOMEN}w4{bcolors.RESET}, {bcolors.WOMEN}w3{bcolors.RESET}, {bcolors.WOMEN}w2{bcolors.RESET}}}")
    print(f"\t{bcolors.MEN}m3{bcolors.RESET}: {{{bcolors.WOMEN}w2{bcolors.RESET}, {bcolors.WOMEN}w1{bcolors.RESET}, {bcolors.WOMEN}w3{bcolors.RESET}, {bcolors.WOMEN}w4{bcolors.RESET}}}")
    print(f"\t{bcolors.MEN}m4{bcolors.RESET}: {{{bcolors.WOMEN}w4{bcolors.RESET}, {bcolors.WOMEN}w2{bcolors.RESET}, {bcolors.WOMEN}w3{bcolors.RESET}, {bcolors.WOMEN}w1{bcolors.RESET}}}")

    print("\nWomen's Preferences:")
    print(f"\t{bcolors.WOMEN}w1{bcolors.RESET}: {{{bcolors.MEN}m4{bcolors.RESET}, {bcolors.MEN}m3{bcolors.RESET}, {bcolors.MEN}m1{bcolors.RESET}, {bcolors.MEN}m2{bcolors.RESET}}}")
    print(f"\t{bcolors.WOMEN}w2{bcolors.RESET}: {{{bcolors.MEN}m2{bcolors.RESET}, {bcolors.MEN}m4{bcolors.RESET}, {bcolors.MEN}m1{bcolors.RESET}, {bcolors.MEN}m3{bcolors.RESET}}}")
    print(f"\t{bcolors.WOMEN}w3{bcolors.RESET}: {{{bcolors.MEN}m4{bcolors.RESET}, {bcolors.MEN}m1{bcolors.RESET}, {bcolors.MEN}m2{bcolors.RESET}, {bcolors.MEN}m3{bcolors.RESET}}}")
    print(f"\t{bcolors.WOMEN}w4{bcolors.RESET}: {{{bcolors.MEN}m3{bcolors.RESET}, {bcolors.MEN}m2{bcolors.RESET}, {bcolors.MEN}m1{bcolors.RESET}, {bcolors.MEN}m4{bcolors.RESET}}}\n")

def print_graphs(data):
    for graph_name, graph_data in data["graphs"].items():
        print(f"\n{graph_name}:")
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
        if graph_name == "Step 6B":
            break
        else:
            print()  # Blank line between graphs

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function: print_description(str)
    Purpose:  Used in print_graphs(), this function prints a description 
              of what is being shown with each graph. Descriptions from: 
              https://www.ams.org/publicoutreach/feature-column/fc-2015-03.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def print_description(graph_name):
    if graph_name == "Step 1A":
        print(f"\nEach man {bcolors.ENGAGED}proposes{bcolors.RESET} to the woman he most prefers:")
        print(f"\t{bcolors.MEN}m1{bcolors.RESET} proposes to {bcolors.WOMEN}w1{bcolors.RESET}")
        print(f"\t{bcolors.MEN}m2{bcolors.RESET} proposes to {bcolors.WOMEN}w1{bcolors.RESET}")
        print(f"\t{bcolors.MEN}m3{bcolors.RESET} proposes to {bcolors.WOMEN}w2{bcolors.RESET}")
        print(f"\t{bcolors.MEN}m4{bcolors.RESET} proposes to {bcolors.WOMEN}w4{bcolors.RESET}\n")
    elif graph_name == "Step 1B":
        print(f"\nNotice that {bcolors.WOMEN}w1{bcolors.RESET} receives proposals from {bcolors.MEN}m1{bcolors.RESET} and {bcolors.MEN}m2{bcolors.RESET}. She")
        print(f"chooses the proposal from {bcolors.MEN}m1{bcolors.RESET} since she prefers {bcolors.MEN}m1{bcolors.RESET} to {bcolors.MEN}m2{bcolors.RESET}.\n")
    elif graph_name == "Step 2A":
        print(f"\nSince {bcolors.MEN}m2{bcolors.RESET} has been rejected by {bcolors.WOMEN}w1{bcolors.RESET}, he {bcolors.ENGAGED}proposes{bcolors.RESET} to his second choice, {bcolors.WOMEN}w4{bcolors.RESET}.\n")
    elif graph_name == "Step 2B":
        print(f"\nNow {bcolors.WOMEN}w4{bcolors.RESET} has proposals from {bcolors.MEN}m2{bcolors.RESET} and {bcolors.MEN}m4{bcolors.RESET} of which she chooses the one from {bcolors.MEN}m2{bcolors.RESET}.\n") 
    elif graph_name == "Step 3A":
        print(f"\n{bcolors.MEN}m4{bcolors.RESET} {bcolors.ENGAGED}proposes{bcolors.RESET} to {bcolors.WOMEN}w2{bcolors.RESET}...\n") 
    elif graph_name == "Step 3B":
        print(f"\nwho accepts the proposal and rejects {bcolors.MEN}m3{bcolors.RESET}.\n") 
    elif graph_name == "Step 4A":
        print(f"\n{bcolors.MEN}m3{bcolors.RESET} {bcolors.ENGAGED}proposes{bcolors.RESET} to {bcolors.WOMEN}w1{bcolors.RESET}...\n") 
    elif graph_name == "Step 4B":
        print(f"\nwho accepts the proposal and rejects {bcolors.MEN}m1{bcolors.RESET}.\n")  
    elif graph_name == "Step 5A":
        print(f"\n{bcolors.MEN}m1{bcolors.RESET} {bcolors.ENGAGED}proposes{bcolors.RESET} to {bcolors.WOMEN}w2{bcolors.RESET}...\n")  
    elif graph_name == "Step 5B":
        print(f"\nwho rejects him because she prefers her current partner, {bcolors.MEN}m4{bcolors.RESET}.\n")  
    elif graph_name == "Step 6A":
        print(f"\n{bcolors.MEN}m1{bcolors.RESET} {bcolors.ENGAGED}proposes{bcolors.RESET} to {bcolors.WOMEN}w3{bcolors.RESET}...\n")  
    elif graph_name == "Step 6B":
        print(f"\nwho accepts his proposal, which is our final marriage.\n")   
    else:
        print("\nWe haven't gotten there yet!\n")

def print_conclusion():
    print("\nResulting Marriages:")
    print_marriages()
    print("\nAs a reminder, our preference lists looked like this:")
    print_preference_lists()
    print("We can see that the resulting marriages have accomplished the goal of solving the Stable")
    print("Marriage Problem: no two individuals prefer each other over their assigned partners.")

def print_sources():
    print("\nSources:")
    print("\n[1]  Austin, David. \"The Stable Marriage Problem and School Choice.\" American Mathematical")
    print("Society, March 2015, https://www.ams.org/publicoutreach/feature-column/fc-2015-03.")
    print("Accessed 20 Nov. 2025.")
    print()
    print("[2]  Microsoft. Github Copilot, GPT-4.1, OpenAI, 2024. Accessed 20 Nov. 2025; Used to")
    print("format graphs and assistance with small debugging tasks.")

def print_marriages():
    print(f"\t{bcolors.MEN}m1{bcolors.RESET} is {bcolors.PROPOSED}married{bcolors.RESET} to {bcolors.WOMEN}w3{bcolors.RESET}")
    print(f"\t{bcolors.MEN}m2{bcolors.RESET} is {bcolors.PROPOSED}married{bcolors.RESET} to {bcolors.WOMEN}w4{bcolors.RESET}")
    print(f"\t{bcolors.MEN}m3{bcolors.RESET} is {bcolors.PROPOSED}married{bcolors.RESET} to {bcolors.WOMEN}w1{bcolors.RESET}")
    print(f"\t{bcolors.MEN}m4{bcolors.RESET} is {bcolors.PROPOSED}married{bcolors.RESET} to {bcolors.WOMEN}w2{bcolors.RESET}")

if __name__ == "__main__":
    main()

