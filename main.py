item_number_collection = []
item_desc_collection = []
item_rprice_collection = []
number_of_bids = []

while True:
  seller_choice = input("Would you like to:\n1. Add item\n2. Proceed to Auction\nType here: ")
 
  try:
    int(seller_choice)
  except:
    print("Choice must be whole numbers!")

  if seller_choice == '1': 
    item_number = input("Enter the item number: ")
    if item_number in item_number_collection:
      print("Choose a different item number")
    else:
      item_desc = input("Enter the item description: ")

      rprice_validation = True
      while rprice_validation == True:
        item_rprice = input("Enter the item reserve price: ")
        try: 
          float(item_rprice)
          rprice_validation = False
        except:
          print("Item reserve price must be in digits")


    item_number_collection.append(item_number)
    item_desc_collection.append(item_desc)
    item_rprice_collection.append(float(item_rprice))

  elif seller_choice == "2":
    if len(item_number_collection) < 2:
      print(f"There must be at least 2 items to proceed to auction. Currently, you have {len(item_number_collection)}")
    
    else:
      break
  else:
    print("\nChoose a number from 1-2")

buyer_name_collection = [] 
highest_bid_collection = []   
        
while True:
  buyer_choice = int(input("\nWould you like to: \n1. Register as a new buyer \n2. Bid on an item \n3. End auction\nType here: "))

  if buyer_choice == 1:
    buyer_name_validation = True
    while buyer_name_validation == True:
      buyer_name = input("Enter your full name: ")
      if buyer_name.title() in buyer_name_collection:
        print("Please enter your name as per IC")
      else:
        buyer_name_collection.append(buyer_name.title())
        buyer_name_validation = False
        print(f"Your buyer number is : {buyer_name_collection.index(buyer_name.title()) + 1}")
        
  elif buyer_choice == 2:

    buyer_identity_validation = True
    while buyer_identity_validation == True:
      buyer_identity = input("Enter your buyer number: ")

      try:
        buyer_name_collection[int(buyer_identity) - 1]
        buyer_identity_validation = False
      except ValueError:
        print("Buyer number must be in digits!")
      except IndexError:
        print("Buyer number does not exist")
      
    for index in range(0, len(item_number_collection)):
      highest_bid_collection.append(0)
      number_of_bids.append(0)
      print(f"\n{index + 1}. \nItem number: {item_number_collection[index]}")
      print(f"Item description: {item_desc_collection[index]}")
      print(f"Highest current bid: {highest_bid_collection[index]}")

    buyer_section = True
    while buyer_section == True:
      item_number_buyerinput = input("Enter the item number you wish to bid on: ")

      if item_number_buyerinput in item_number_collection:
        validation_bid_amount = True

        while validation_bid_amount == True:

          index = item_number_collection.index(item_number_buyerinput)
          bid_amount_buyer_input = input("Enter the amount you wish to bid: ")
          
          try:
            if float(bid_amount_buyer_input) > highest_bid_collection[index]:
              highest_bid_collection[index] = float(bid_amount_buyer_input)
              number_of_bids[index] += 1
              validation_bid_amount = False
              buyer_section = False
            else: 
              print("Bid amount must be more than the current bid")

          except:
            print("Bid amount must be in digits!")

      else:
        print("Please enter the item number correctly")

  elif buyer_choice == 3:
    fee_amount = 1.1
    fee = []
    unreached_highestbid = []
    nobids = []

    for index in range(0, len(item_number_collection)):
      if highest_bid_collection[index] >= item_rprice_collection[index]:
        sold = list(item_number_collection[index])
        fee.append(highest_bid_collection[index] * fee_amount)
        totalfee = sum(fee)
        number_of_sold = len(sold)
      
      elif number_of_bids[index] != 0 and highest_bid_collection[index] < item_rprice_collection[index]:
        unreached_itemnumber = list(item_number_collection[index])
        unreached_highestbid.append(highest_bid_collection[index])
        number_of_unreached = len(unreached_itemnumber)

      else:
        nobids.append(item_number_collection[index])
        number_of_nobids = len(nobids)



    print(f"The total fee is {totalfee}") 
    print(f"The items that have not reached their reserve price are {unreached_itemnumber}, with their highest bids of {unreached_highestbid} respectively")
    print(f"The items that have received no bids are {nobids}")
    print(f"The number of items sold are {number_of_sold}")
    print(f"The number of items that did not reach their reserve price are {number_of_unreached}")
    print(f"The number of items that did not receive any bids are {number_of_nobids}")

  else:
    print("Please choose a number from 1-3")
        
    

