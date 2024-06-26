import os

tool = "Teeth"
money = 0

def start_game():
  os.system("clear")
  
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

    if (choice.lower() == "k" and tool.lower() == "teeth"):
      money += 1
    elif (choice.lower() == "k" and tool.lower() == "rusty scissors"):
      money += 5
    elif (choice.lower() == "k" and tool.lower() == "old-timey push lawnmower"):
      money += 50
    elif (choice.lower() == "k" and tool.lower() == "fancy battery-powered lawnmower"):
      money += 100 
    elif (choice.lower() == "k" and tool.lower() == "team of starving students"):
      money += 250
    elif (choice.lower() == "l"):
      shop_item1 = itemDetails("Rusty Scissors")
      shop_item2 = itemDetails("Old-timey Push Lawnmower")
      shop_item3 = itemDetails("Fancy Battery-powered Lawnmower")
      shop_item4 = itemDetails("Team of Starving Students")

      buy_tool = input(f"*** SHOP ***\nWhich item would you like to buy? Press the items number then Enter\n\n1: Rusty Scissors\nQuantity:{shop_item1['quantity']} Price:${shop_item1['item_price']}\n\n2: Old-timey Push Lawnmower\nQuantity:{shop_item2['quantity']} Price:${shop_item2['item_price']}\n\n3: Fancy Battery-powered Lawnmower\nQuantity:{shop_item3['quantity']} Price:${shop_item3['item_price']}\n\n4: Team of Starving Students\nQuantity:{shop_item4['quantity']} Price:${shop_item4['item_price']}\n\nPress ANY OTHER KEY to EXIT SHOP\n> ")

      if tool.lower() != "rusty scissors" and buy_tool == "1" and money >= shop_item1['item_price']:
        money -= shop_item1['item_price']
        tool = "Rusty Scissors"
      elif tool.lower() != "old-timey push lawnmower" and buy_tool == "2" and money >= shop_item2['item_price']:
        money -= shop_item2['item_price']
        tool = "Old-timey Push Lawnmower"
      elif tool.lower() != "fancy battery-powered lawnmower" and buy_tool == "3" and money >= shop_item3['item_price']:
        money -= shop_item3['item_price']
        tool = "Fancy Battery-powered Lawnmower"
      elif tool.lower() != "team of starving students" and buy_tool == "4" and money >= shop_item4['item_price']:
        money -= shop_item4['item_price']
        tool = "Team of Starving Students"
    elif choice == "q":
      return exit()
    else:
      start_game()
    
    if money >= 1000 and tool.lower() == "team of starving students":
      print(f"Money: {money}")
      print("You won!")
      exit()

    while choice.lower() != "q":
      start_game()
  
  def print_stats():
    os.system("clear")
    print(f"Money: {money}")
    print(f"Current Tool: {tool}")

  print_stats()
  user_choice = input("\nPress 'k' then Enter to start cutting lawns\nPress 'l' then Enter to open shop\nPress 'q' then Enter to QUIT GAME\n\n> ")

  player_move(user_choice)

def intro():
    print("It's a great day to start a business..\n")
    print("I'm going to start a landscaping business!\n")
    print("WELCOME TO LANDSCAPER TERMINAL GAME\n")

    print("You are starting a landscaping business. You need to cut lawns and grow your business money bank. If you make enough, you can purchase tools that earn more money!\n")

    start_menu_selection = input("Press space then Enter to START\nPress 'q' then Enter to QUIT GAME\n\n> ")

    if (start_menu_selection == " "):
      start_game()
    elif (start_menu_selection == "q"):
      exit()
    else:
      os.system("clear")
      print("INVALID OPTION. TRY AGAIN!")
      intro()

intro()