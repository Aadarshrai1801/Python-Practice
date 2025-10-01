import random

import os

from BlindAuction_art import logo
print(logo)

def clear_screen() :
    os.system('cls')

def find_highest_bidder(bidding_record) :
    highest_bid = 0
    winner = ""
    for bidder in bidding_record :
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} and his bid amount is ${highest_bid}.")    

auction_dictionary = {}

def auction(name1,bid1) :   
    auction_dictionary[name1] = bid1

should_continue = True
while should_continue :
    name = input("What is your name? :\n")

    bid = int(input("What is your bid? : \n$"))
    
    auction(name, bid)

    auction_continue = input("Are there any bidders? Type 'yes' or 'no'.\n").lower()
    

    if auction_continue == "no" :
        should_continue = False
        print(auction_dictionary)

        find_highest_bidder(auction_dictionary)

    elif auction_continue == "yes" :
        clear_screen()    
        