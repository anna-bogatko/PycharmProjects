"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.
"""

# def net_income(state_income, gross_income):
#     print((gross_income - state_income) * 0.1)
#
# net_income(100, 200)

def calculateNetIncome(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross Income
    :param state: State Name
    :return: Net Income
    """

    state_tax = {"LA": 10, "NY": 9, "TX": 0, "SA": 5}

    #Calculate Net Income after federal tax
    net = gross - (gross * .10)

    #Calculate Net Income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all heavy taxes is  " + str(net))
        return net
    else:
        print("State is not in the list")
        return None

calculateNetIncome(20000, 'SA')



