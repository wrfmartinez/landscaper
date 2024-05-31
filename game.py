tool = "teeth"
day = 1
money = 0
quantity = 0

def main():
  def intro():
    print("It's a great day to start a business..\n")
    print("I'm going to start a landscaping business!\n")
    print("WELCOME TO LANDSCAPER TERMINAL GAME\n")

  def itemDetails(item):
    dict = {
      "quantity": 1,
      "item_price": 0
    }

    if item == "Rusty Scissors":
      dict["item_price"] = 5
    elif item == "Old-timey Push Lawnmower":
      dict["item_price"] = 25
    elif item == "Fancy Battery-powered Lawnmower":
      dict["item_price"] = 250
    elif item == "Team of Starving Students":
      dict["item_price"] = 500

    return dict

  def player_move(choice):
    if (choice.lower() == "k" and tool == "teeth"):
      global money
      money += 1
    elif (choice.lower() == "l"):
      shop_item1 = itemDetails("Rusty Scissors")
      shop_item2 = itemDetails("Old-timey Push Lawnmower")
      shop_item3 = itemDetails("Fancy Battery-powered Lawnmower")
      shop_item4 = itemDetails("Team of Starving Students")

      buy_tool = input(f"*** SHOP ***\nWhich item would you like to buy?\nRusty Scissors Quantity:{shop_item1['quantity']} Price:${shop_item1['item_price']}\n")
    else:
      return exit()
    
    while choice.lower() != "q":
      main()
  
  def print_stats():
    print(f"Money: {money}")
    print(f"Current Tool: {tool}")

  print_stats()
  user_choice = input("\nPress 'k' to start cutting lawns\nPress 'l' to open shop\nPress 'q' to quit\n\n> ")

  player_move(user_choice)

main()