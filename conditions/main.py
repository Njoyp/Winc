# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

"""
factors
weather
    rainy
    sunny
    windy
    neutral

time_of_day
    day
    night

cows_need_milking
    need milking: True
    dont need milking: False

location_cows
    pasture
    cowshed
   
season
    winter
    spring
    summer
    fall

slurry_tank
    full: True
    not full: False

grass_status
    long: True
    short: False
"""


# action 1 
""" 
take cows to cowshed

This needs to be done when one or more of the following statements are true:

The cows are on the pasture at night
The cows are standing in the rain
"""

def cows_to_cowshed (location_cows, time_of_day, weather):
    if location_cows == "pasture" and time_of_day == "night" :
        return "Take the cows to cowshed\n"
    if weather == "rainy" and location_cows == "pasture" : 
        return "Take the cows to cowshed\n"
    else:
       return "The cows can stay where they are\n"
""""
print ("The cows are on the pasture and it's nighttime")    # cowshed    
print (cows_to_cowshed("pasture", "night", ""))

print ("The cows are on the pasture and it's daytime") # no cowshed
print (cows_to_cowshed("pasture", "day", ""))

print ("The cows are on the pasture and it's rainy") # cowshed
print (cows_to_cowshed("pasture", "day", "rainy"))

print ("The cows are in the cowshed and it's rainy") # no cowshed
print (cows_to_cowshed("cowshed", "day", "rainy"))
"""
# action 2
""" 
milk cows

This needs to be done when the cows require milking, but is only possible when:

The cows are in the cowshed
"""

def milk_cows (cows_need_milking, location_cows) :
    if cows_need_milking == True and location_cows == "cowshed" :
        return "The cows can be milked right now\n"
    else: 
        return "The cows can't be milked right now\n"
"""
print ("The cows are in the cowshed and ready to be milked") # milk cows
print (milk_cows(True, "cowshed"))

print ("The cows are in the cowshed but not ready to be milked") # don't milk cows
print (milk_cows(False, "cowshed"))

print ("The cows are ready to be milked but are on the pasture") # don't milk cows
print (milk_cows(True, "pasture"))
"""
# action 3
"""
fertilize pasture

This needs to be done when the slurry tank is full, but is only possible when:

The cows are in the cowshed
The weather is not sunny or windy
"""

def fertilize_pasture (slurry_tank_full, location_cows, weather):
    if (slurry_tank_full == True and location_cows == "cowshed" and (weather != "sunny" and weather != "windy")) : 
        return "The pasture can be fertilized\n"
    else:
        return "The pasture can't be fertilized right now\n"
"""
print ("Its windy, the cows are in the cowshed en and the slurry tank is full") # not fertilize
print ( fertilize_pasture(True, "cowshed", "windy"))

print ("It's raining, the cows are in the cowshed and the slurry tank is full") # ferilize
print (fertilize_pasture(True, "cowshed", "rainy"))

print ("It's sunny, the cows are on the pasture and the slurry tank is full") # not fertilize
print (fertilize_pasture(True, "pasture", "sunny"))

print ("It's sunny, the cows are on the cowshed and the slurry tank is full") # not fertilize
print (fertilize_pasture(True, "cowshed", "sunny"))

print ("It's rainy, the cows are in the cowshed and the slurry tank is empty") # not fertilize 
print ( fertilize_pasture(False, "cowshed", "rainy"))

print ("The weather is neutral, the cows are in the cowshed and the slurry tank is full") # fertilize
print (fertilize_pasture (True, "cowshed", "neutral"))
"""

# action 4
""" 
mow grass

This needs to be done when all of the following are true:

The grass is long
It's spring
The weather is sunny
But is only possible when:

The cows are not on the pasture
"""
def mow_grass (grass_status_long, season, weather, location_cows):
    if (grass_status_long == True and season == "spring" and weather == "sunny" and location_cows != "pasture"):
        return "The grass needs to be mowed right now and the grass can be mowed right now\n"
    if (grass_status_long == True and season == "spring" and weather == "sunny" and location_cows == "pasture"):
        return "The grass needs to be mowed right now but the grass can't be mowed right now\n"
    else:
        return "The grass doesn't need to be mowed right now\n"
""""  
print ("The grass is long, it is spring, the weater is sunny and the cows are not on the pasture") # needs mowing and can be mowed
print (mow_grass(True, "spring", "sunny", "cowshed"))

print ("The grass is long, it's spring, it's sunny, but the cows are on the pasture") # need mowing but can't be mowed
print (mow_grass(True, "spring", "sunny", "pasture"))

print ("The grass is long, it's summer, it's sunny and the cows are in the cowshed") # doesn't need mowing
print (mow_grass(True, "summer", "sunny", "cowshed"))

print ("The grass is short, it's spring, it's sunny and the cows are in the cowshed") # doesn't need mowing
print (mow_grass(False, "spring", "sunny", "cowshed"))

print ("The grass is long, it's spring, the weather is neutral and the cows are in the cowshed") #doesn't need mowing
print (mow_grass(True, "spring", "neutral", "cowshed"))
"""
# action 4
"""
wait

This is done when no other action applies.

Write a function farm_action that takes the seven factors as arguments in the order they are listed above, 
and returns a single string containing the action(s) the farmer should take.

You can assume the given arguments are of the correct type, but you should not assume their values are one of the known possible values. 
It's possible your function will receive a weather argument with value ping-pong ball.

However, your implementation of farm_action should return the actions exactly as listed.

By default the function should only return one action per function call. To decide which action to return look at the order they were listed on this page. 
For example: if the conditions for both "milk cows" and "mow grass" are met you should only take the action(s) necessary for "milk cows" because 
it has higher priority.

Under some combination of conditions the function needs to return multiple actions. This happens when (1) cows can be milked, (2) the land can be fertilized 
or
(3) the grass can be mown. If we need to do one of those things AND the cows are in the pasture we need to add an action before and after our "main" action. 
The action before is take cows to cowshed, the action after is take cows back to pasture. But be careful: if the cows were already in the cowshed, 
they should not be taken back to the pasture.

The format for returning multiple actions is to return a string with each action on its own line, in order. The last line should not end on a newline.
"""


def farm_action (weather, time_of_day, cows_need_milking, location_cows, season, slurry_tank_full, grass_status_long):
    if weather == "rainy" and cows_need_milking == False and location_cows == "pasture" : 
        return "take cows to cowshed"
    if time_of_day == "night" and cows_need_milking == False and location_cows == "pasture":
        return "take cows to cowshed"
   
    if cows_need_milking == True and location_cows == "cowshed":
        return "milk cows"     
    if cows_need_milking == True and location_cows == "pasture":
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
        
    if weather == "rainy" and cows_need_milking == True and location_cows == "pasture":
        return "take the cows to cowshed\nmilk the cows"
    if time_of_day == "night" and cows_need_milking == True and location_cows == "pasture": 
        return "take the cows to cowshed\nmilk the cows"

    if (slurry_tank_full == True and location_cows == "cowshed" and (weather != "sunny" and weather != "windy")):
        return "fertilize pasture"
    if (slurry_tank_full == True and location_cows == "pasture" and (weather != "sunny" and weather != "windy")):
        return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"

    if (grass_status_long == True and season == "spring" and weather == "sunny" and location_cows != "pasture"):
        return "Mow grass"
    if (grass_status_long == True and season == "spring" and weather == "sunny" and location_cows == "pasture" and time_of_day != "night"):
        return "Take cows to cowshed\nMow grass\ntake cows back to pasture"
    else:
        return "wait"

print (farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print (farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print (farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print (farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))

