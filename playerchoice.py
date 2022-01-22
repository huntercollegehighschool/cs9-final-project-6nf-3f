def playerchoice():
  PlayerChoice = input("Input 1 for Rock, 2 for Paper, 3 for Scissors: ")
  if PlayerChoice !="1" and PlayerChoice !="2" and PlayerChoice !="3":
    print("That's not a valid input.")
    return "Restart"
  elif PlayerChoice == "1":
    return "Rock"
  elif PlayerChoice == "2": 
    return "Paper"
  elif PlayerChoice == "3":
    return "Scissors"