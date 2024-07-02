import hashlib

# By law they are required to give me their govt issued id and their name
# for me to keep on record for law purporsus

# I can use that information to make unique ids for when that person comes in
# and gives me the requried inforimation and I look them up on my systems.

# def build_buy_sell_item(itemName = 'none', itemDescription, itemQuality, retailValue, customerId='None'):
    
    # item = {
    #     'itemName': 'value1',
    #     'itemDescription': 'value2',
    #     'itemQuailty': 1,
    #     'retailValue': 50
    #     'transactionId':hash(utcTimestamp, customerId)
    # }

    # return item
    # pass

def build_customer_profile_item(firstName, lastName, govtIdNumber, height=-1, weight=-1, race="none"):

    print("about to create thte item")
    hash_object = hashlib.sha256()
    hash_object_string = hash_object.str(firstName+lastName+govtIdNumber).hexdigest(),

    # Created the hash object
    item = {
        "firstName":firstName,
        "lastName":lastName,
        "govtIdNumber":govtIdNumber,
        "height":height,
        "weight":weight,
        "race":race,
        "storeIdNumber":hash_object_string
        }

    return item

