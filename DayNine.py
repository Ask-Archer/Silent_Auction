from replit import clear
from art import logo
print(logo)

bids = {}
#create an empty dictionary to hold the bids
bidding_finished = False
#Create a false variable for the while not statement

def find_highest_bidder(bidding_record):
  #You cannot use the same name as the empty dictionary listed above (bids), because that dictionary is instead going to be used later. Create a new dictionary
  highest_bid = 0
  winner = ""
  #create two empty variables. one as an empty string for the name of the winner. another set to 0 for the winners bid. We will assign these empty variables to other variables later on
  # bidding_record = {"Angela": 123, "James": 321}
  #create a for loop for the keys in the bidding_record
  for bidder in bidding_record:
    #bidding_record is a dictionary and its key is assigned in this for loop as bidder
    bid_amount = bidding_record[bidder]
    #you want to name the value in the dictionary (bidding_record) for future use. (The value is what you attach to the key within the dictionary.) The above is how you do so.
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
      #You're trying to find the highest bid (which would be equivalent to the value in the dictionary) and the bidder that bid it (winner) (which would be equivalent to the key). 
      #So take the two empty variables mentioned (a string and an integer) before and set them equal to the key (bidder) and the value (bid_amount) of the dictionary 
      #Remember, when using a for loop for a dictionary, the name for the key for the dictionary is always set between "for" and "in"
  print(f"The winner is {winner} with a bid of ${highest_bid}")

#Remember this (below) is a loop. (It is outside of the find_highest_bid fucnction.) It will keep going for as long as the condition allows.
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  #this is where you ask the user questions. ask for the inputs of the bidders name and their price
  bids[name] = price
  #name = dictionary key
  #price = dictionary value
  #this is how you add everything to the dictionary. the dictionary key is set to whatever the users 'name' is, its value is set to the 'price'
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  #This is the part where the True/False variable comes in that goes with the while loop. The user kind of controls the while loop here. So long as the user states that there are other bidders, the while loop repeats. 
  if should_continue == "no":
    bidding_finished = True
    #The while loop ends because bidding_finished returns True
    find_highest_bidder(bids)
    #What we want to happen after the user is done inputting the keys (bidder) and values (bid_amount) into the dictionary, is for the computer to find the highest bidder along with the highest bid and we do that using the find_highest_bidder function we created before 
  elif should_continue == "yes":
    clear()
    #This means the loop will repeat, ostensibly
