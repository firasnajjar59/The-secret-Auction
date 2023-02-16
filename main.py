import os
from art import logo

bids={}
def add_bid(name,bid_value):
    bids[name]=bid_value
more_bids=True
while more_bids:
    os.system("cls")
    print(logo)
    name=input("What's your name?\n")
    bid=int(input("What's your bid?\n$"))
    add_bid(name,bid)
    continue_bids=input("Are there any other bidders? Type 'y' or 'n'.\n").lower()
    if continue_bids=="n":
        more_bids=False
temp=""
for key in bids:
    if len(temp)>0:
        if bids[key]>bids[temp]:
            temp=key
    else:
        temp=key
print(f"\nThe winner is {temp} with a bid of ${bids[temp]}")
