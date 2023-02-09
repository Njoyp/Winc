# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
# Part one Create Passport

# date_of_birth = date.birth()
# date_of_birth_str = date_of_birth.isoformat()

# countries = get_countries oproepen door countries []

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport_info = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": float(height),
        "nationality": nationality 
        }
    return passport_info

print(create_passport("Nikita", "01-07-1993", "Amsterdam", 1.69, "The Netherlands"))

passport_Bea = create_passport("Bea", "09-08-1994", "Amsterdam", 1.59, "The Netherlands")
print(passport_Bea)

def add_stamp(passport, country):
  if country == passport["nationality"]:
    return passport
    
  if "stamps" not in passport:
    passport["stamps"] = []

  if country not in passport["stamps"]:
    passport["stamps"].append(country)

  return passport

print(add_stamp(passport_Bea, "Belgium"))

def add_biometric_data (passport):
  passport["biometric"]  

"""
Explantion

As you may know, governments are often strapped for programming talent. But you're coming to the rescue! 
You are going to write a tool that creates and checks passport information.

We already supplied a list of countries in countries.json and a function get_countries in helpers.py 
that fetches and returns this list.

Part 1: Create Passport
Write in main.py a function create_passport that takes as its arguments, in this order:
A name (str)
A date of birth (str in ISO 8601 format, for example: 2002-12-31)
A place of birth (str)
A height in meters (float)
A nationality (str)

And returns a passport dict containing this information with the keys:
name
date_of_birth
place_of_birth
height
nationality

⚠️ Note:
We express a nationality as a country (str) from the list returned by get_countries.

Part 2: Add Stamp
Whenever a person travels to another country, they get a stamp in their passport that shows that they have been there. 
Implement add_stamp in main.py, which takes as its arguments, in this order:
A passport (dict) like the one returned by create_passport
A country (str)

And:
Adds or updates a key-value pair:
(key) 'stamps'
(value) a list of countries (str) that the person has been to.
Finally: add_stamp returns the (possibly) stamped passport.

Note:
Any stamp may be a person's first stamp, in which case the 'stamps' key in their passport dict is not present yet. 
You will have to create it in that case. But beware not to overwrite people's existing stamps list!
Travellers don't need stamps of their home country.
No duplicate stamps! If a traveler already has a stamp for a country, don't give them another stamp.

Part 3: Add biometric data
Passport technology advances and security has become more of a concern for a lot of countries. 
Quite a few countries have added "biometric data" to passports. See this Wikipedia(opens in a new tab) 
article for more information (you won't need that for this exercise).

Because the software you're writing will be used by different countries that want to add different kinds of 
biometric data your code needs to be able to handle all kinds of different biometric data.

Write a function add_biometric_data in main.py that takes as its arguments, in this order:

A passport (dict) like the one returned by create_passport
A name (str) for the type of biometric data that will be added.
The value, or values of the to-be-added biometric data.
A date in ISO format YYYY-MM-DD (str) for when the biometric data was recorded.
The biometric data should live in a dictionary inside of the passport. In other words: a nested dictionary. The key for the biometric data dictionary is biometric.

The function should return:
If the passport did not yet have any biometric data: add the key for it, you can assume 
you'll only get passports with a chip to save biometric data.
If the type of biometric data was not yet in the passport: add it to the passport.
The value for the specific type of biometric data should again be a dictionary (so nested again). 
This dictionary should have two keys: date and value. See examples below for specific examples.
If the type of biometric data was already in the passport: update the biometric data in the passport, 
overwriting the previous value and date.
"""
