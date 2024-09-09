import random
import difflib
import keyword
attacker_list = ["Striker", "Deimos", "Ram", "Brava", "Grim", "Sens", "Osa", "Flores", "Zero", "Ace", "Iana", "Kali", "Amaru", "Nokk", "Gridlock", "Nomad", "Maverick", "Lion", "Finka", "Dokkaebi", \
"Zofia", "Ying", "Jackal", "Hibana", "Capitao", "Blackbeard", "Buck", "Sledge", "Thatcher", "Ash", "Thermite", "Montagne", "Twitch", "Blitz", "IQ", "Fuze", "Glaz"]
defender_list = ["Skopos", "Sentry", "Tubarao", "Fenrir", "Solis", "Azami", "Thorn", "Thunderbird", "Aruni", "Melusi", "Oryx", "Wamai", "Goyo", "Warden", "Mozzie", "Kaid", "Clash", "Maestro", \
"Alibi", "Vigil", "Ela", "Lesion", "Mira", "Echo", "Caveria", "Valkyrie", "Frost", "Mute", "Smoke", "Castle", "Pulse", "Doc", "Rook", "Jager", "Bandit", "Tachanka", "Kapkan"]
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!               !!!!!!!!!!!!!!!\n"
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!           !!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!                      !!!!!!!!        !!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!                       !!!!!!!!       !!!!!!                !!!!!!\n"
"!!!!!!                        !!!!!!!!      !!!!!!                !!!!!!\n"
"!!!!!!                        !!!!!!!!      !!!!!!\n"
"!!!!!!                        !!!!!!!!      !!!!!!\n"
"!!!!!!                        !!!!!!!!      !!!!!!\n"
"!!!!!!                        !!!!!!!!      !!!!!!\n"
"!!!!!!                       !!!!!!!!       !!!!!!\n"
"!!!!!!                      !!!!!!!!!       !!!!!!\n"
"!!!!!!                     !!!!!!!!!        !!!!!!!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        !!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!         !!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!                     !!!!!!           !!!!!!                 !!!!!\n"
"!!!!!!                      !!!!!!          !!!!!!                 !!!!!\n"
"!!!!!!                       !!!!!!         !!!!!!                 !!!!!\n"
"!!!!!!                        !!!!!!        !!!!!!                 !!!!!\n"
"!!!!!!                         !!!!!!       !!!!!!                 !!!!!\n"
"!!!!!!                          !!!!!!      !!!!!!                 !!!!!\n"
"!!!!!!                           !!!!!!        !!!!!!!!!!!!!!!!!!!!!!!!!\n"
"!!!!!!                            !!!!!!          !!!!!!!!!!!!!!!!!!!")
print()
print("***Enter atk and def names starting with a capital and use no special characters***")
print()
print("Examples -> Capitao Ying Sledge Tubarao")
print()
atkban1 = ""
atkban2 = ""
defban1 = ""
defban2 = ""
def suggest_atk_words(atkban1, atkban2):
 atk1_suggestions = difflib.get_close_matches(atkban1, attacker_list, n=5, cutoff=0.3)
 atk2_suggestions = difflib.get_close_matches(atkban2, attacker_list, n=5, cutoff=0.3)
 if atk1_suggestions:
  print(f"Name not found. Maybe you meant: {', '.join(atk1_suggestions)}")
  print()
 elif atk2_suggestions:
  print(f"Name not found. Maybe you meant: {', '.join(atk2_suggestions)}")
  print()
 else:
  print("Name not found. No similar matches found. Please try again.")
  print()
def suggest_def_words(defban1, defban2):
 def1_suggestions = difflib.get_close_matches(defban1, defender_list, n=5, cutoff=0.3)
 def2_suggestions = difflib.get_close_matches(defban2, defender_list, n=5, cutoff=0.3)
 if def1_suggestions:
  print(f"Name not found. Maybe you meant: {', '.join(def1_suggestions)}")
  print()
 elif def2_suggestions:
  print(f"Name not found. Maybe you meant: {', '.join(def2_suggestions)}")
  print()
 else:
  print("Name not found. No similar matches found. Please try again.")
  print()
print()
atkban1 = str(input("Enter attack ban 1: "))
print()
while atkban1 not in attacker_list:
 suggest_atk_words(atkban1, attacker_list)
 atkban1 = str(input("Enter attack ban 1: "))
 print()
atkban2 = str(input("Enter attack ban 2: "))
print()
while atkban2 not in attacker_list:
 suggest_atk_words(atkban2, attacker_list)
 atkban2 = str(input("Enter attack ban 2: "))
 print()
defban1 = str(input("Enter defense ban 1: "))
print()
while defban1 not in defender_list:
 suggest_def_words(defban1, defender_list)
 defban1 = str(input("Enter defense ban 1: "))
 print()
defban2 = str(input("Enter defense ban 2: "))
print()
while defban2 not in defender_list:
 suggest_def_words(defban2, defender_list)
 defban2 = str(input("Enter defense ban 2: "))
player_count = int(input("How many players are there? "))
print()
player1 = ""
player2 = ""
player3 = ""
player4 = ""
player5 = ""
if player_count == 1:
 player1 = str(input("Enter player 1's name: "))
elif player_count == 2:
 player1 = str(input("Enter player 1's name: "))
 player2 = str(input("Enter player 2's name: "))
elif player_count == 3:
 player1 = str(input("Enter player 1's name: "))
 player2 = str(input("Enter player 2's name: "))
 player3 = str(input("Enter player 3's name: "))
elif player_count == 4:
 player1 = str(input("Enter player 1's name: "))
 player2 = str(input("Enter player 2's name: "))
 player3 = str(input("Enter player 3's name: "))
 player4 = str(input("Enter player 4's name: "))
else:
 player1 = str(input("Enter player 1's name: "))
 player2 = str(input("Enter player 2's name: "))
 player3 = str(input("Enter player 3's name: "))
 player4 = str(input("Enter player 4's name: "))
 player5 = str(input("Enter player 5's name: "))
rando1 = ""
rando2 = ""
rando3 = ""
rando4 = ""
rando5 = ""
round_counter = 0
while True:
 print()
 side_check = str(input("Are you on atk or def? "))
 continue_check = "y"
 while side_check == "atk" and continue_check == "y": #Attacker random select starts here
  while (player_count == 1) and (continue_check == "y"):
   rando1 = random.choice(attacker_list)
   if (rando1 != atkban1) and (rando1 != atkban2):
    print(f"\n{player1} is: {rando1}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 2) and (continue_check == "y"):
   rando1 = random.choice(attacker_list)
   rando2 = random.choice(attacker_list)
   if (rando1 != atkban1) and (rando1 != atkban2) and (rando2 != atkban1) and (rando2 != atkban2) and (rando1 != rando2):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 3) and (continue_check == "y"):
   rando1 = random.choice(attacker_list)
   rando2 = random.choice(attacker_list)
   rando3 = random.choice(attacker_list)
   if (rando1 != atkban1) and (rando1 != atkban2) and (rando2 != atkban1) and (rando2 != atkban2) and (rando3 != atkban1) and (rando3 != atkban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 4) and (continue_check == "y"):
   rando1 = random.choice(attacker_list)
   rando2 = random.choice(attacker_list)
   rando3 = random.choice(attacker_list)
   rando4 = random.choice(attacker_list)
   if (rando1 != atkban1) and (rando1 != atkban2) and (rando2 != atkban1) and (rando2 != atkban2) and (rando3 != atkban1) and (rando3 != atkban2) and (rando4 != atkban1) and (rando4 != atkban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3) and (rando1 != rando4) and (rando2 != rando4) and (rando3 != rando4):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    print(f"{player4} is: {rando4}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 5) and (continue_check == "y"):
   rando1 = random.choice(attacker_list)
   rando2 = random.choice(attacker_list)
   rando3 = random.choice(attacker_list)
   rando4 = random.choice(attacker_list)
   rando5 = random.choice(attacker_list)
   if (rando1 != atkban1) and (rando1 != atkban2) and (rando2 != atkban1) and (rando2 != atkban2) and (rando3 != atkban1) and (rando3 != atkban2) and (rando4 != atkban1) and (rando4 != atkban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3) and (rando1 != rando4) and (rando2 != rando4) and (rando3 != rando4) and (rando5 != atkban1) and (rando5 != atkban2) and (rando1 != rando5)\
   and (rando2 != rando5) and (rando3 != rando5) and (rando4 != rando5):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    print(f"{player4} is: {rando4}\n")
    print(f"{player5} is: {rando5}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
 while side_check == "def" and continue_check == "y": #Defender random select starts here
  while (player_count == 1) and (continue_check == "y"):
   rando1 = random.choice(defender_list)
   if (rando1 != defban1) and (rando1 != defban2):
    print(f"\n{player1} is: {rando1}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 2) and (continue_check == "y"):
   rando1 = random.choice(defender_list)
   rando2 = random.choice(defender_list)
   if (rando1 != defban1) and (rando1 != defban2) and (rando2 != defban1) and (rando2 != defban2) and (rando1 != rando2):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 3) and (continue_check == "y"):
   rando1 = random.choice(defender_list)
   rando2 = random.choice(defender_list)
   rando3 = random.choice(defender_list)
   if (rando1 != defban1) and (rando1 != defban2) and (rando2 != defban1) and (rando2 != defban2) and (rando3 != defban1) and (rando3 != defban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 4) and (continue_check == "y"):
   rando1 = random.choice(defender_list)
   rando2 = random.choice(defender_list)
   rando3 = random.choice(defender_list)
   rando4 = random.choice(defender_list)
   if (rando1 != defban1) and (rando1 != defban2) and (rando2 != defban1) and (rando2 != defban2) and (rando3 != defban1) and (rando3 != defban2) and (rando4 != defban1) and (rando4 != defban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3) and (rando1 != rando4) and (rando2 != rando4) and (rando3 != rando4):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    print(f"{player4} is: {rando4}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
  while (player_count == 5) and (continue_check == "y"):
   rando1 = random.choice(defender_list)
   rando2 = random.choice(defender_list)
   rando3 = random.choice(defender_list)
   rando4 = random.choice(defender_list)
   rando5 = random.choice(attacker_list)
   if (rando1 != defban1) and (rando1 != defban2) and (rando2 != defban1) and (rando2 != defban2) and (rando3 != defban1) and (rando3 != defban2) and (rando4 != defban1) and (rando4 != defban2) and (rando1 != rando2)\
   and (rando1 != rando3) and (rando2 != rando3) and (rando1 != rando4) and (rando2 != rando4) and (rando3 != rando4) and (rando5 != defban1) and (rando5 != defban2) and (rando1 != rando5)\
   and (rando2 != rando5) and (rando3 != rando5) and (rando4 != rando5):
    print(f"\n{player1} is: {rando1}\n")
    print(f"{player2} is: {rando2}\n")
    print(f"{player3} is: {rando3}\n")
    print(f"{player4} is: {rando4}\n")
    print(f"{player5} is: {rando5}\n")
    round_counter += 1
    continue_check = str(input("Enter y to do another pick or press enter: "))
   else:
    continue_check = "y"
 if round_counter >= 4: #New game input starts here
  print()
  new_game = str(input("Would you like to start a new game? Type y for yes or n for no: "))
  print()
  if (new_game == "y"):
   atkban1 = str(input("Enter attack ban 1: "))
   print()
   while atkban1 not in attacker_list:
    suggest_atk_words(atkban1, attacker_list)
    atkban1 = str(input("Enter attack ban 1: "))
    print()
   atkban2 = str(input("Enter attack ban 2: "))
   print()
   while atkban2 not in attacker_list:
    suggest_atk_words(atkban2, attacker_list)
    atkban2 = str(input("Enter attack ban 2: "))
    print()
   defban1 = str(input("Enter defense ban 1: "))
   print()
   while defban1 not in defender_list:
    suggest_def_words(defban1, defender_list)
    defban1 = str(input("Enter defense ban 1: "))
    print()
   defban2 = str(input("Enter defense ban 2: "))
   print()
   while defban2 not in defender_list:
    suggest_def_words(defban2, defender_list)
    defban2 = str(input("Enter defense ban 2: "))
    print()
   round_counter = 0
   player_reset = str(input("Would you like to reset player count? Type y for yes or n for no: "))
   print()
   if (player_reset == "y"):
    player_count = int(input("How many players are there? "))
    print()
    if player_count == 1:
     player1 = str(input("Enter player 1's name: "))
    elif player_count == 2:
     player1 = str(input("Enter player 1's name: "))
     player2 = str(input("Enter player 2's name: "))
    elif player_count == 3:
     player1 = str(input("Enter player 1's name: "))
     player2 = str(input("Enter player 2's name: "))
     player3 = str(input("Enter player 3's name: "))
    elif player_count == 4:
     player1 = str(input("Enter player 1's name: "))
     player2 = str(input("Enter player 2's name: "))
     player3 = str(input("Enter player 3's name: "))
     player4 = str(input("Enter player 4's name: "))
    else:
     player1 = str(input("Enter player 1's name: "))
     player2 = str(input("Enter player 2's name: "))
     player3 = str(input("Enter player 3's name: "))
     player4 = str(input("Enter player 4's name: "))
     player5 = str(input("Enter player 5's name: "))
  
   
 
 
 
 
