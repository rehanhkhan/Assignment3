'''*********************************************************************************************************************************
8-8. User Albums: Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
*********************************************************************************************************************************'''

def make_album(artisit_name,album_title,tracks=0):
    """Return a dictionary of information about a album."""
    if(tracks):
        album = {'Name': artisit_name, 'Title': album_title,'Tracks':tracks}
    else:
        album = {'Name': artisit_name, 'Title':album_title}

    return album

code = 1
while(code==1):
    code = int(input("To create Album please enter code 1 and to quit enter code 2 : "))
    if (code==1):
        name = input('Please Enter Artist Name :')
        title = input('Please Enter Title of Album :')
        track = int(input('Please Enter No of Tracks in Album :'))
        album = make_album(name.title(),title.title(),track)
        print('Following album is build as per your input \n ' + str(album) + '\n')

