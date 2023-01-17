# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# part one
leek_price = 2

cost_leek = "Leek is " + str(leek_price) + " euro per kilo."

print (cost_leek)

# part two
order_four_leek = "'leek 4'"
amount_leek = int(order_four_leek [order_four_leek.find(str(4))])

# print (amount_leek)
# print(type(amount_leek))

sum_total = amount_leek * leek_price
print (sum_total)

#part three
broccoli_price = 2.34 # euro per kilo
broccoli_order = 1.6 # kg
total_broccoli = broccoli_price * broccoli_order

#print (total_broccoli)

final_broccoli = str(broccoli_order) + "kg broccoli costs " + str(round(total_broccoli,2)) + "e"
print (final_broccoli)