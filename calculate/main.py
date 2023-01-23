# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
"""
1) 
Create a variable for each of the following items in the supermarket: broccoli, leek, potato and brussel_sprout. 
Broccoli and leek are 2 euros a piece, a potato is 3 euros and a Brussels sprout will set you back 7 euros. Times are hard.

2) Calculate the total cost if you were to buy one of each -- not by hand, of course, let Python do it! Store this in a variable sum_one_each.

3) Calculate the average price per item and store this in avg_price.

4) Create a variable num_potatoes that indicates we want 7 potatoes. Do the same for:
num_broccolis -- we want 5 of those.
num_leeks -- 2 please.
num_brussel_sprouts -- we'll take 10.

5) Calculate the sum total and store it in a variable aptly named sum_total.

6) Fortunately for us, there's a discount of 30%. Store this in a variable discount_percentage (hint: note the variable name already says 'percent')

7) Calculate the amount owed after the discount is applied, rounded to the nearest cent. Store the result in discounted_sum_total.

8) Print this amount.
"""
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = broccoli + leek + potato + brussel_sprout

avg_price = sum_one_each / 4

num_potatoes = 7 
num_broccolis = 5 
num_leeks = 2 
num_brussel_sprouts = 10 

sum_total = (num_potatoes * potato) + (num_broccolis * broccoli) + (num_leeks * leek) + (num_brussel_sprouts * brussel_sprout)

discount_percentage = 30

discounted_sum_total = sum_total * (1 - (discount_percentage/100))

print (discounted_sum_total)