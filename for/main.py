from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
"""
1) shortest_names: takes a list of country names and returns a list of country names that have the shortest length. 
If there is only one country with the shortest name the list will contain only that country name, 
otherwise multiple countries should be in the list. 
Use a for-loop and len!
"""
def shortest_names (countries): 
   shortest = min(countries, key=len)
   shortes_names_list = [] # list die je wil vullen
   for country in countries:
      if len(country) == len(shortest):
         shortes_names_list.append(country) # hier vul je de lijst
   return shortes_names_list # hier print je de lijst met korste namen

"""
2) most_vowels: takes a list of country names and returns a list with the top three countries that have the most 
vowels in their name. The country with the most vowels should be on position 0 in the list, 
the country with the second-most on position 1, and so on. If there are multiple countries with the same number 
of vowels the order does not matter. 
To sidestep the y-issue: we count aeiou as vowels.
"""

def most_vowels_first (countries):
   return sum([countries.count(x) for x in "aeiouAEIOU"])

def most_vowels (countries):
   return sorted(countries, reverse= True, key = most_vowels_first)[:3]

"""
3) alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
Solutions with 14 or fewer countries are accepted as correct.

"""

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
   countries = get_countries()
   print (shortest_names (countries))
   print(most_vowels(countries))

""" Write the calls to your functions here. """
