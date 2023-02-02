from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(requested_amount):
    facts = [] #deze lijst ga je invullen
    i = 0 #iteration zelfde als loop
    while len(facts) < requested_amount:
        fact = random_koala_fact()
        if fact not in facts: #zorgt dat je geen dubbele feiten krijgt
            facts.append(fact)
        if i == 1000: break #zorgt dat ie niet infinate is
        i += 1
    #print(len(facts))
    return facts

def num_joey_facts(): #returns how many facts contain joey
    first_fact = random_koala_fact()
    times_seen_first_fact = 0 
    joey_facts = 0
    unique_joey_facts = []

    while times_seen_first_fact < 10:
        fact = random_koala_fact()
        if first_fact == fact:
            times_seen_first_fact += 1
        if fact not in unique_joey_facts:
            unique_joey_facts.append(fact)
            if "joey" in fact.lower():
                joey_facts += 1
    return joey_facts

def koala_weight (): # return hoeveel koala in kg weegt als integer
    fact = random_koala_fact()
    while "kg" not in fact.lower():
        fact = random_koala_fact() # als feit er niet inzit wil ik een nieuw feitje
    """
    split = fact.split ("kg")[0]
    second_split = split.split(" ")
    weight = second_split [-1]
    return int(weight)
    """
    return int(fact.split("kg")[0].split(" ")[-1]) # dit zijn de stappen die hier direct bovenstaan

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    #print(random_koala_fact())
    #print (unique_koala_facts(10))
    #print (num_joey_facts())
    print(koala_weight())

"""
We are preparing a fun family night with a quiz. The youngest kid in the family is currently a massive fan of koalas, 
so we compiled a list of koala facts and wrote a function random_koala_fact that you can use in main.py.

Write the following functions by making use of while and random_koala_fact:

1) unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list. 
Note that there are only a limited number of unique facts in the dataset. For high arguments your function should 
try to return all unique facts in the dataset. No worries: the number of facts is small enough that this should be 
feasible. You can set an iteration limit of 1000.

2) num_joey_facts: young marsupials are called 'joeys'. How many unique facts mentioning this term are in our facts 
dataset? Count them by getting facts from random_koala_fact until you have seen some particular fact 10 times, 
then return how many unique joey facts you counted in the dataset.

3) koala_weight: somewhere in the data is a fact about how heavy a koala is. This function should return that weight 
in kilogram (kg) as an integer.
"""