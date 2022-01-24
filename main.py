
"""
Name: Oscar Turner (James abandoned to do his own project)
Name of Project: Special Rock Paper Scissors
"""
import random
from playerchoice import playerchoice
from saysomething import saysomething
from numberofgames import howmanygames



print("Hello.")
# functions start here
a = saysomething
def onegame(): 
  speech = saysomething()
  if speech == "roll":
    list_choices = ["Rock", "Rock", "Rock", "Paper", "Scissors"]   
  elif speech == "crush":
    list_choices = ["Rock", "Paper", "Paper", "Scissors"]
  else:
    list_choices = ["Rock", "Paper", "Scissors"]
  ComputerC = (random.choice(list_choices))
  PlayerC = playerchoice()
  if PlayerC == "Restart":
    onegame()
  elif ComputerC == "Rock":
    if PlayerC == "Rock":
      print("Tie")
      return "Tie"
    elif PlayerC == "Paper":
      print("Win")
      return "Win"
    elif PlayerC == "Scissors":
      print("Loss")
      return "Loss"
  elif ComputerC == "Paper":
      if PlayerC == "Paper":
        print("Tie")
        return "Tie"
      elif PlayerC == "Rock":
        print("Loss")
        return "Loss"
      elif PlayerC == "Scissors":
        print("Win")
        return "Win"
  elif ComputerC == "Scissors":
    if PlayerC == "Rock":
      print("Win")
      return "Win"
    elif PlayerC == "Paper":
      print("Loss")
      return "Loss"
    elif PlayerC == "Scissors":
      print("Tie")
      return "Tie"

def bestthreeoffive():
  Pscore = 0
  Cscore = 0
  while Pscore < 3 and Cscore < 3:
    result = onegame()
    if result == "Tie":
      print("Player Score:", Pscore)
      print("Computer Score:", Cscore)
    if result == "Win": #Not sure if these have to / should be elifs
      Pscore = Pscore + 1
      print("Player Score:", Pscore)
      print("Computer Score:", Cscore)
    if result == "Loss":
      Cscore = Cscore + 1
      print("Player Score:", Pscore)
      print("Computer Score:", Cscore)
  if Pscore == 3:
    return "Player Wins!"
  elif Cscore == 3: 
    return "Computer Wins!"




x = howmanygames()
if x == 1:
  onegame()
elif x == 5:
  ab = bestthreeoffive()
  print(ab)
