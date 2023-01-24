# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
"""
Composer John Williams has written a great many pieces for a lot of different films. He's written so many, in fact, 
that he has asked you to write a number of functions to help him keep it all organized.

1) Write a function alphabetical_order that takes one argument: a list of strings that represent film names. 
It returns a list of the same films in alphabetical order. We have not discussed sorting lists yet, so you should probably 
search the web to see if there's a good approach out there. Your solution should not be longer than a few lines.

2) Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
    This page will come in handy: Wikipedia -- List of awards and nominations received by John Williams
    A nomination is not a win.
    You are not allowed to do string-to-string comparisons in this function, so no string_a == string_b!
    John is not very tidy with his archive, so the captitalization of the names might not be correct. 
    Look into using the lower-function on the given film string.

3) John's son Joseph accidentally mixed in some of his own work as lead singer for Toto with a list of his dad's compositions. 
Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list.
    Use this information: Wikipedia -- Joseph Williams (musician)
    It is not certain that all of Joseph's Toto albums are in the list received by remove_toto_albums, but they might! Don't let your script run into any errors.
    Joseph did not inherit his dad's sloppiness with capitalization, so his Toto albums would be listed correctly.
    Search the web on how to remove an item from a list by value.

"""

# alphabetical_order film list

def alphabetical_order (movies):
    return (sorted(movies))

# movies = ["b", "a", "c"]
# movies = ["Saving Private Ryan", "The River","Checkmate", "Star Wars - Main Title", "The Poseidon Adventure", "Cinderella Liberty", "Tom Sawyer", "Jaws", "Star Wars: Episode IV - A New Hope", "E.T the Extra-Terrestrial", "Memoirs of a Geisha"]

print(alphabetical_order(["Saving Private Ryan", "The River","Checkmate", "Star Wars - Main Title", "The Poseidon Adventure", "Cinderella Liberty", "Tom Sawyer", "Jaws", "Star Wars: Episode IV - A New Hope", "E.T the Extra-Terrestrial", "Memoirs of a Geisha"]))


# golden globe and use lower-function
""""
def won_golden_globe(movie_name):
    if movie_name in ["Jaws", "Star Wars: Episode IV - A New Hope", "E.T the Extra-Terrestrial", "Memoirs of a Geisha"]:
        print(True)
    else:
        print (False)

won_golden_globe("Jaws")
won_golden_globe("Jeff")
 """

# remove Joseph's toto albums
"""
def remove_toto_albums(album):
    for x in album:
        return (x)

albums =["Africa", "World on a String", "Fahrenheit", "Jaws"]



remove_toto_albums("Africa")
#remove_toto_albums = []
#films.remove(emove_toto_albums = [])

def remove_toto_albums(album):
    for x in album:
        x.remove()

albums =["Africa", "World on a String", "Fahrenheit", "Jaws"]

remove_toto_albums("Africa")
# stuurt lijst mee in functies met films en toto albums geen loop gebruiken met if statement naam toto album in operator naamlijst.remove(wat je verwijderd)
"""