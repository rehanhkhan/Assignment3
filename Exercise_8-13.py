'''*********************************************************************************************************************************
8-13. User Profile: Start with a copy of user_profile.py from page 153.
Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
*********************************************************************************************************************************'''

def build_profile(first, last, **other_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in other_info.items():
        profile[key] = value.title()
    return profile

my_profile = build_profile('rehan', 'hameed', location='karachi',field='Data Science', hobby='Play Cricket' )
print(my_profile)

