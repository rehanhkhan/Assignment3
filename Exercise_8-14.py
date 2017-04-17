'''*********************************************************************************************************************************
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
*********************************************************************************************************************************'''

def car_info(manufacturer, model_name, **other_info):
    """Build a dictionary containing everything we know about a cars."""
    car_Profile = {}
    car_Profile['manufacturer'] = manufacturer.title()
    car_Profile['model'] = model_name.title()
    for key, value in other_info.items():
        car_Profile[key] = value
    return car_Profile

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)

