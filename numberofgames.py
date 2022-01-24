def howmanygames():
  from playerchoice import playerchoice
  from saysomething import saysomething
  from main import onegame
  from main import bestthreeoffive
  numberofgames = (input("Input 1 to play 1 game or 5 to play best 3 out of 5: "))
  if numberofgames.isnumeric():
    numberofgames = int(numberofgames)
  else:
    print("That's not a valid input.")
    howmanygames()

  
  if numberofgames != 1 and numberofgames !=5:
    print("That's not a valid input.")
    howmanygames()
  elif numberofgames == 1:
    return 1
  elif numberofgames == 5:
    return 5