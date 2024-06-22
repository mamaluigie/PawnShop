import numpy as np


class item:

    def __init__(self):
        self.item_price = self.generateRandomItemWithValue()
        # Calculated by taking the standard deviations for the past 12 months 
        # in a sliding window of 3 months.
        self.average_3_month_volatility = 

    # Generating the random item values based on the above
    def generateRandomItemValue():
        # Set up the random items being created as a random number between the ranges below
        items = [np.random.choice([x for x in range(1001, 5000)]),
        np.random.choice([x for x in range(501, 1000)]),
        np.random.choice([x for x in range(201, 500)]),
        np.random.choice([x for x in range(101, 200)]),
        np.random.choice([x for x in range(0, 100)])]

        # To simulate a skewed curve for items that are cheaper are going to come in 
        # more often before I get the gun license. Once I get the gun license this value will prob go up
        return np.random.choice(items, 1, p=(0.1, 0.2, 0.3, 0.25, 0.15))