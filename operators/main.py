# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# The language spoken the most in Switzerland is the same as in Spain.
spain_spoken_language = "Castilian Spanish"
switzerland_spoken_language = "German" or "Swiss German"

print(spain_spoken_language == switzerland_spoken_language)

# The most prevalent religion in Switzerland is the same as in Spain.
spain_prevalent_religion = "Roman Catholic"
switzerland_prevalent_religion = "Roman Catholic"

print(spain_prevalent_religion == switzerland_prevalent_religion)

# The name length of Spain's capital does not equal that of Switzerland.
spain_capital_name = len("Madrid")
switzerland_capital_name = len("Bern")

print(spain_capital_name != switzerland_capital_name) 
# or print (spain_capital_name == switzerland_capital_name)

# Switzerland's GDP is greater than Spain's GDP.
spain_GDP = 1798 # billion in dollars 2021
switzerland_GDP = 618.228 # billion in dollars 2021

print (switzerland_GDP > spain_GDP)

# The population growth is less than 1% in Switzerland and Spain.
spain_population_growth = 0.13
switzerland_population_growth = 0.65

print (spain_population_growth < 1 and switzerland_population_growth < 1)

# total population
spain_total_population = 47163418 # 2022
switzerland_total_population = 8508698 # 2022

# At least one of the two countries has a population count of over 10 million.
print(spain_total_population > 10000000 or switzerland_total_population > 10000000)

# Exactly one of the two countries has a population count of over 10 million.
#print (spain_total_population > 10000000 | switzerland_total_population > 10000000) | wordt gebruikt voor binary nummers
print(switzerland_total_population > 10000000 or spain_total_population > 10000000 
and switzerland_total_population < 10000000 or spain_total_population < 10000000)
