# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

"""factors
weather
    rainy
    sunny
    windy
    neutral

time_of_day
    day
    night

cow milking status
    need milking: True
    dont need milking: False

location_of_the_cows
    pasture
    cowshed
   
season
    winter
    spring
    summer
    fall

slurry tank
    full: True
    not full: False

grass status
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
"""
def cows_to_cowshed (location_cows, time_of_day, weather):
    if location_cows == "pasture" and time_of_day == "night" :
        return "Take the cows to cowshed\n"
    elif weather == "rainy" and location_cows == "pasture" : # or can this just be an if?
        return "Take the cows to cowshed\n"
    else:
       return "The cows can stay where they are\n"

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
"""
def milk_cows (cow_milking_status, location_cows) :
    if cow_milking_status == True and location_cows == "cowshed" :
        return "The cows can be milked right now\n"
    else: 
        return "The cows can't be milked right now\n"

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
    if (slurry_tank_full == True and location_cows == "cowshed" and (weather != "sunny" or weather != "windy")) :  # how to get both sunny and windy correctly in this line?
        return "The pasture can be fertilized\n"
    else:
        return "The pasture can't be fertilized right now\n"

print ("Its windy, the cows are in the cowshed en and the slurry tank is full") # not fertilize
print ( fertilize_pasture(True, "cowshed", "windy"))

print ("It's raining, the cows are in the cowshed and the slurry tank is full") # ferilize
print (fertilize_pasture(True, "cowshed", "rainy"))

print ("It's sunny, the cows are on the pasture and the slurry tank is full") # not fertilize
print (fertilize_pasture(True, "pasture", "sunny"))

print ("It's windy, the cows are in the cowshed and the slurry tank is empty") # not fertilize 
print ( fertilize_pasture(False, "cowshed", "windy"))