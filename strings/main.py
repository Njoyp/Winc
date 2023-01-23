# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# part one
"""
1) Create a variable for every player that scored, for example:
example = 'Gut von Examplestein'

2) Create a variable for each minute of the match that a goal was scored in, for example:
goal_0 = 32

3) Using the +-operator, create a string that reports on who scored when, according to the format:
<scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
The result should be stored in a variable scorers

4) Use f-strings or the +-operator to create a single string with information about who scored when in the format:
<scorer_name> scored in the <when_they_scored>nd minute
<scorer_name> scored in the <when_they_scored>th minute
The result should be stored in a variable report.
"""
first_goal = "Ruud Gullit"
second_goal = "Marco van Basten"

goal_0 = 32 # minutes into the match
goal_1 = 54 # minutes into the match

scorers = first_goal + str(goal_0) + ", " + second_goal + str(goal_1)


report = first_goal + "scored in the " + str(goal_0) + "nd minute"  + "\n" + second_goal + "scored in the " + str(goal_1) + "th minute"

# new na feedback
# report = f" {first_goal} scored in the {goal_0}nd minute \n {second_goal} scored in the {goal_1}th minute"

# print (report)

# part two
"""
1) Choose a player that played in the soccer match and store his name as a string in the variable player.

2) first_name: use slicing and the find-method (help(opens in a new tab)) to isolate and store the player's first name.

3) last_name_len: use find, slicing and len to isolate and store the length of their last name.

4) name_short: isolate and store the player's name in this format:
G. von Examplestein

5) chant: this is what the crowd chants when it looks like your player is going to score a goal 
-- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. 
Because Gut has 3 letters in his name, we repeat his name 3 times. Make sure the last character of this string is not a space! For our example player:

Gut! Gut! Gut!

6) good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). 
This variable needs to be a boolean, not a string. You can create the value for this variable by comparing the last character of chant with a space character.
Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).
"""
player = "Ronald Koeman"
first_name = player [player.find ("Ronald"):6]

last_name_len = len (player [player.find ("Koeman"):])

name_short = player[player.find ("Ronald")] + ". " + player [player.find ("Koeman"):]

length_first_name= len(first_name)

chant = ((first_name + "!" + " ") * length_first_name ).strip()

good_chant = chant [-1] != " "

# print (first_name)
# print (last_name_len)
# print (chant)