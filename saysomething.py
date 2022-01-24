#"Professional Rock Paper Scissors Players" (interesting title) often say things to one anoother to subconosciously influence one anothers' choices, so I added something of the sort here. 
def saysomething():
  PlayerSpeech = input("What would you like to say to your opponent? Input 1 for 'Let's roll', 2 to say nothing, 3 to say 'I'm crushing you.' " )
  if PlayerSpeech != "1" and PlayerSpeech != "2" and PlayerSpeech != "3":
    print("That's not a valid input.")
    saysomething()
  elif PlayerSpeech == "1":
    return "roll"
  elif PlayerSpeech == "2":
    return "standard"
  elif PlayerSpeech == "3":
    return "crush"