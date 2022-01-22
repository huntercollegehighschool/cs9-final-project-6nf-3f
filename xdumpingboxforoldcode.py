def computerchoice():
  CompChoice = (random.choice(list_choices))
  return CompChoice

def game():
  PlayerC = playerchoice()
  if PlayerC == "Restart":
    game()
  ComputerC = computerchoice()
  if ComputerC == "Rock":
    if PlayerC == "Rock":
      return "Tie"
    elif PlayerC == "Paper":
      return "Win"
    elif PlayerC == "Scissors":
      return "Loss"
  elif ComputerC == "Paper":
      if PlayerC == "Paper":
        return "Tie"
      elif PlayerC == "Rock":
        return "Loss"
      elif PlayerC == "Scissors":
       return "Win"
  elif ComputerC == "Scissors":
    if PlayerC == "Rock":
      return "Win"
    elif PlayerC == "Paper":
      return "Loss"
    elif PlayerC == "Scissors":
      return "Tie"

def best(a, b):
  while a < 3 and b < 3:
    result1 = onegame()
    if result1 == "Tie":
      return 0
    elif result1 == "Win":
      return 1 # for player
    elif result1 == "Loss":
      return 2 # for computer