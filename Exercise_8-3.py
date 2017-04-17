'''*********************************************************************************************************************************
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''

def make_shirt(size,message):
    '''function takes size as (Small, Medium, Large and Extra Large) \n and message as string argument \n and display shirt according to given size and message'''
    print('Shirt made of size ' + str(size) + " with message written on it as " + message)

#Calling function with positional arguments
make_shirt('Medium',"Champion")

#Calling function with keyword arguments
make_shirt(message="Levis", size='Large')

help(make_shirt)