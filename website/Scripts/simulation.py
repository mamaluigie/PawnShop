import pandas as pd
import scipy as sc
from matplotlib import pyplot as plt
import numpy

# The main idea of this program is to simulate pawnshop returns on a basis of having it 
# be 334 dollars per day on buy/sell and having the buy/sell maturity date be 18 days.

# The loan is going to be a 2 month loan with 25% on the principle per month.
# I will be giving out $334 on average for the items also. 
# Also when the items that are cheaper:
# - $50-$500 I am going to only do like 20% loan for the retail price of the item.

# Also note that in the 3 month period, 3 because there is 2 months that will acrue interest
# 70% of people are not going to be able to pay their loan and will default. 
# Depending on the initial loan price we can caluclate the retail price for the item and see what kind of profit
# I can get on that item in x number of days.

# Idea for assigning interest to the items will be consistant
# $0-$500 25% interest
# $501-$1500 20% interest
# $1501 - $5000 10% interest
# $5001 - $10,000 5% intetest

# maybe for the design to make two objects that have a attributes that correspond to if that corresponds to 
# items being bought and items being loaned on pawn.

# Each can reference different stats values for how the business traffic is happening.






def main():




if __name__ == '__main__':
    main()