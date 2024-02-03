import random

def roll():
  min_value=1
  max_value=6
  roll=random.randint(min_value,max_value)

  return roll


while True:
  players=input("Enter the number of players (2-4)")
  if players.isdigit():
     #isdigit() :checks if the variable is a number
     players=int(players)
     if 2<= players <= 4:
         break
     else:
        print("Must be between 2-4 players.")
  else:
    print("Invalid,try again")      

max_score=50
player_scores= [0 for _in range(players)]   
#0 for _in range():puts a zero in the list for each player we have

while max(player_scores) < max_score:
   
   for player_idx in range(players):
       current_score=0

       while True:
           should_roll=input("Would you like to roll (y/n)?")
           if should_roll.lower() != "y":
                break

           value=roll()
           if value==1:
                print("You have rolled a 1! Turn done!")
                break
           else:
                current_score += value
                print("You rolled a:",value)

        player_scores[player_idx] += current_score       

