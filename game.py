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
    global money
    global tool

    if (choice.lower() == "k" and tool == "teeth"):
      money += 1
    elif (choice.lower() == "k" and tool == "rusty scissors"):
      money += 5
    elif (choice.lower() == "k" and tool == "old-timey push lawnmower"):
      money += 50
    elif (choice.lower() == "k" and tool == "fancy battery-powered lawnmower"):
      money += 100 
    elif (choice.lower() == "k" and tool == "team of starving students"):
      money += 250
    elif (choice.lower() == "l"):
      shop_item1 = itemDetails("Rusty Scissors")
      shop_item2 = itemDetails("Old-timey Push Lawnmower")
      shop_item3 = itemDetails("Fancy Battery-powered Lawnmower")
      shop_item4 = itemDetails("Team of Starving Students")

      buy_tool = input(f"*** SHOP ***\nWhich item would you like to buy?\n1: Rusty Scissors Quantity:{shop_item1['quantity']} Price:${shop_item1['item_price']}\n2: Old-timey Push Lawnmower Quantity:{shop_item2['quantity']} Price:${shop_item2['item_price']}\n3: Fancy Battery-powered Lawnmower Quantity:{shop_item3['quantity']} Price:${shop_item3['item_price']}\n4: Team of Starving Students Quantity:{shop_item4['quantity']} Price:${shop_item4['item_price']}\n\n> ")

      if buy_tool.lower() == "1" and money == shop_item1['item_price']:
        tool = "rusty scissors"
      elif buy_tool.lower() == "2" and money == shop_item2['item_price']:
        tool = "old-timey push lawnmower"
      elif buy_tool.lower() == "3" and money == shop_item3['item_price']:
        tool = "fancy battery-powered lawnmower"
      elif buy_tool.lower() == "4" and money == shop_item4['item_price']:
        tool = "team of starving students"
    elif money == 1000:
      print("You won!")
      exit()
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