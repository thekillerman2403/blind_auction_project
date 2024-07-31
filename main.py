from replit import clear
from art import logo
print(logo)
name = input("What is your name? ")
bid = int(input("What is your bid? $"))
bidders = {}
bidders[name] = bid
more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
while more_bidders == "yes":
  clear()
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bidders[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

highest_bid = 0
highest_bidder = ""
for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bid = bidders[bidder]
    highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")