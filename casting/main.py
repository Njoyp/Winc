# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# part one
"""
1) Create a variable leek_price with an integer value of 2.

2) Cast this into a string and use the +-operator to print a string like this one, only with the correct price in it:
'Leek is 50 euro per kilo.'
"""
leek_price = 2

cost_leek = "Leek is " + str(leek_price) + " euro per kilo."

print (cost_leek)

# part two
"""
1) We got an order for four leeks! Store the string 'leek 4' in a variable.

2) Use find and slicing to extract the number from this string.

3) Cast it into an integer.

4) Use this and leek_price to compute the sum total and store it in sum_total. Print out the value for this variable.
"""
order_four_leek = "'leek 4'"
amount_leek = int(order_four_leek [order_four_leek.find(str(4))])

# print (amount_leek)
# print(type(amount_leek))

sum_total = amount_leek * leek_price
print (sum_total)

#part three
"""
Broccoli costs 2.34 euros per kg. We got an order: 'broccoli 1.6'.

1) Create one variable for the broccoli price and one for the order.

2) Compute the total price for this order.

3) Use the +-operator to assemble and print a string that looks like the following:
'1.6kg broccoli costs 500.34e'
"""
broccoli_price = 2.34 # euro per kilo
broccoli_order = 1.6 # kg
total_broccoli = broccoli_price * broccoli_order

#print (total_broccoli)

final_broccoli = str(broccoli_order) + "kg broccoli costs " + str(round(total_broccoli,2)) + "e"
print (final_broccoli)