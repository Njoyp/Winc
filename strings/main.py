# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# part one
first_goal = "Ruud Gullit "
second_goal = "Marco van Basten "

goal_0 = 32 # minutes into the match
goal_1 = 54 # minutes into the match

scorers = first_goal + str(goal_0) + ", " + second_goal + str(goal_1)

report = first_goal + "scored in the " + str(goal_0) + "nd minute"  + "\n" + second_goal + "scored in the " + str(goal_1) + "th minute"


# part two
player = "Ronald Koeman"
first_name = player [player.find ("Ronald"):6]

last_name_len = len (player [player.find ("Koeman"):])

name_short = player[player.find ("Ronald")] + ". " + player [player.find ("Koeman"):]

length_first_name= len(first_name)

chant = ((first_name + "!" + " ") * length_first_name ).strip()

good_chant = chant [-1] != " "

