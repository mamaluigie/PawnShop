import random
import numpy as np
# 5-10 customers per day
# 20% chance I can do a deal with one of them wanting a loan or selling something
# using the distribution see what kind of item it would be coming in.


# I can do business with 1 of them

# Test case for chances of the person having an item of that value
# 10%: $1001-$5000
# 20%: $501-$1000
# 30%: $201-$500
# 25%: $101-$200
# 15%: $0-$100

# Generating the random item values based on the above
def generateRandomItemWithValue():

    # Set up the random items being created as a random number between the ranges below
    items = [np.random.choice([x for x in range(1001, 5000)]),
    np.random.choice([x for x in range(501, 1000)]),
    np.random.choice([x for x in range(201, 500)]),
    np.random.choice([x for x in range(101, 200)]),
    np.random.choice([x for x in range(0, 100)])]

    # To simulate a skewed curve for items that are cheaper are going to come in 
    # more often before I get the gun license. Once I get the gun license this value will prob go up
    return np.random.choice(items, 1, p=(0.1, 0.2, 0.3, 0.25, 0.15))


# This will return if a customer comes with something to bring to the table to sell or pawn
def getBuySellCustomer():
    # 50 percent chance I can get a deal out of them
    if (random.random() > 0.5):

        item = generateRandomItemWithValue()
        bought_item = item * .75
        return item
        
    else:
        return 0

# Returns a tuple with the loan amount and interest rate according to the chart
def getPawnLoanCustomer():

    interest_ammount_list = {
         "$501-$5000":0.10,
         "$301-$500":0.20,
         "$201-$300":0.30,
         "$101-$200":0.25,
         "$0-$100":0.15
    }
    # 50 percent chance I can get a deal out of them
    if (random.random() > 0.5):
        item = generateRandomItemWithValue()

        # Find out where the interest lies
        for rangestr in interest_ammount_list.keys():
            # split rangestr into two values
            range1, range2 = rangestr.replace("$", "").split("-")
            range1 = int(range1)
            range2 = int(range2)

            # Check if the item value is between the two values 
            if (item >= range1 and item <= range2):
                pecentage_interest = interest_ammount_list[rangestr]



# Gets the customer with 50/50 chacne that it will be a pawn customer or a buy/sell
def getCustomer():
    # 20% chance the customer is 

    if (random.random() > 0.2):
        if random.random() > 0.5:
            return getBuySellCustomer()
        else:
            return getPawnLoanCustomer()

    return None

