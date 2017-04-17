'''*********************************************************************************************************************************
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.
*********************************************************************************************************************************'''


def make_shirt(size='Large',message='I love Python'):
    '''function takes size as (Small, Medium, Large and Extra Large) with default as Large
       \n and message as string argument with default value 'I love Python
       \n and display shirt according to given size and message'''
    print('Shirt made of size ' + str(size) + " with message written on it as \"" + message + '\"')

#Calling function with defualt message
make_shirt(size='Medium')

#Calling function with all default values
make_shirt()

make_shirt('small','I love Data Science')

