'''*********************************************************************************************************************************
8-9. Magicians: Make a list of magician’s names.
    Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
    Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name.
    Call show_magicians() to see that the list has actually been modified.
8-11. Unchanged Magicians: Start with your work from Exercise 8-10.
    Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged,
    return the new list and store it in a separate list.
    Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.
*********************************************************************************************************************************'''

magicians = ['Akber','Salman','Qaisar']

def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())

# call function to show names of Magicians in list
show_magicians(magicians)

def make_great(magicians_list):
    for i in range(0,len(magicians_list)):
        magicians_list[i] = 'Great ' + magicians_list[i]
    return magicians_list


# Call function to make magicians great
make_great(magicians)

# call function to show names of Magicians name changes in orginal list
show_magicians(magicians)

#call function with new list to keep orginal list unchanged
new_magitions = make_great(magicians[:])

#Call function to show orginal magicians list keep its position
show_magicians(magicians)

#Call function to show new magicians list with aditional value
show_magicians(new_magitions)
