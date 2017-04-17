'''*********************************************************************************************************************************
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
If the calling line includes a value for the number of tracks, add that value to the album’s dictionary.
Make at least one new function call that includes the number of tracks on an album.
*********************************************************************************************************************************'''

def make_album(artisit_name,album_title,tracks=0):
    """Return a dictionary of information about a album."""
    if(tracks):
        album = {'Name': artisit_name, 'Title': album_title,'Tracks':tracks}
    else:
        album = {'Name': artisit_name, 'Title':album_title}

    return album

album1 = make_album('Atif Aslam','zindagi')
album2 = make_album('Ali Zafar','Chhano',3)
album3 = make_album('Haddiqa','album',2)

print(album1)
print(album2)
print(album3)

