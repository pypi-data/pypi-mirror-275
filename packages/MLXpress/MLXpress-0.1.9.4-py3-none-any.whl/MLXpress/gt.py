def gt1(file_name):
    """
    Creates a new Python file with the specified name and writes the given code to it.

    Parameters:
    file_name (str): The name of the Python file to be created.
    """
    code1 = """\
def prisoner_dilemma(player1_choice, player2_choice):
    payoff_matrix = {
        ('cooperate', 'cooperate'): (-1, -1),
        ('cooperate', 'defect'): (-3, 0),
        ('defect', 'cooperate'): (0, -3),
        ('defect', 'defect'): (-2, -2)
    }
    player1_payoff, player2_payoff = payoff_matrix[(player1_choice, player2_choice)]
    return player1_payoff, player2_payoff

# Players' strategies
player1_choice = 'cooperate'
player2_choice = 'defect'

# Get payoffs
player1_payoff, player2_payoff = prisoner_dilemma(player1_choice, player2_choice)

# Display results
print("Player 1 payoff:", player1_payoff)
print("Player 2 payoff:", player2_payoff)
    """
    try:
        with open(file_name, 'w') as file:
            file.write(code1)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def gt2(file_name):
    code2 = """
# Define the payoffs for each player in the Prisoner's Dilemma
player1_payoffs = [[-1, -3],  # Player 1: Cooperate, Player 2: Cooperate/Defect
                   [0, -2]]   # Player 1: Defect, Player 2: Cooperate/Defect
player2_payoffs = [[-1, 0],   # Player 2: Cooperate, Player 1: Cooperate/Defect
                   [-3, -2]]  # Player 2: Defect, Player 1: Cooperate/Defect

# Function to print payoffs with context
def print_payoffs(player1_payoffs, player2_payoffs):
    choices = ["Cooperate", "Defect"]

    print("Payoff Matrix for the Prisoner's Dilemma:")
    print("Format: (Player 1's Payoff, Player 2's Payoff)\\n")

    for i, choice1 in enumerate(choices):
        for j, choice2 in enumerate(choices):
            print(f"Player 1 {choice1}, Player 2 {choice2}: ({player1_payoffs[i][j]}, {player2_payoffs[i][j]})")

    print("\\nPlayer 1's Payoffs Matrix:")
    for row in player1_payoffs:
        print(row)

    print("\\nPlayer 2's Payoffs Matrix:")
    for row in player2_payoffs:
        print(row)

# Print the payoffs with context
print_payoffs(player1_payoffs, player2_payoffs)
    """
    try:
        with open(file_name, 'w') as file:
            file.write(code2)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def gt3(file_name):
    code3 = """
import numpy as np

player1_payoffs = np.array([[3, 1],
                            [0, 2]])
player2_payoffs = np.array([[3, 0],
                            [1, 2]])

nash_eqs = np.argwhere((player1_payoffs == np.max(player1_payoffs)) & 
                       (player2_payoffs == np.max(player2_payoffs)))

print("Nash Equilibrium(s):")
for eq in nash_eqs:
    print(f"Player 1 chooses strategy {eq[0] + 1}, Player 2 chooses strategy {eq[1] + 1}")
    """
    try:
        with open(file_name, 'w') as file:
            file.write(code3)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def gt4(file_name):
    code4 = """
class GameTreeNode:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


root = GameTreeNode("Root")

decision1 = GameTreeNode("Decision 1")
decision2 = GameTreeNode("Decision 2")
root.add_child(decision1)
root.add_child(decision2)

outcome1 = GameTreeNode("Outcome A", value=10)   
outcome2 = GameTreeNode("Outcome B", value=20)   
decision1.add_child(outcome1)
decision1.add_child(outcome2)

decision3 = GameTreeNode("Decision 3")
decision4 = GameTreeNode("Decision 4")
decision2.add_child(decision3)
decision2.add_child(decision4)

outcome3 = GameTreeNode("Outcome C", value=15)   
outcome4 = GameTreeNode("Outcome DDD", value=25) 
outcome5 = GameTreeNode("Outcome EE", value=25)  
outcome6 = GameTreeNode("Outcome F", value=5)   
decision3.add_child(outcome3)
decision3.add_child(outcome4)
decision4.add_child(outcome5)
decision4.add_child(outcome6)

# Solving the game with a more complex criterion
def solve_game(node):
    if len(node.children) == 0:
        return node.name, node.value
    else:
        child_outcomes = [solve_game(child) for child in node.children]
        # Choose the child with the maximum value and then by longest name as a tiebreaker
        optimal_child = max(child_outcomes, key=lambda x: (x[1], len(x[0])))
        return optimal_child

optimal_outcome_name, optimal_outcome_value = solve_game(root)
print("Optimal Outcome:", optimal_outcome_name, "with value:", optimal_outcome_value)
    """
    try:
        with open(file_name, 'w') as file:
            file.write(code4)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")



