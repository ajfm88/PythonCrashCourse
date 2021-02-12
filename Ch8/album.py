#Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Use None to add an optional parameter to make_album() that allows you to
#store the number of songs on an album. If the calling line includes a value for
#the number of songs, add that value to the album’s dictionary. Make at least
#one new function call that includes the number of songs on an album

def make_album(artist_name, album_title, tracks=0):
    """Return a dictionary of information about an album"""
    album = {'artist': artist_name.title(), 'album': album_title.title(),}
    if tracks:
        album['tracks'] = tracks
    return album

music_1 = make_album('green day', 'american idiot', tracks=14)
print(music_1)

music_2 = make_album('red hot chili peppers', 'stadium arcadium')
print(music_2)

music_3 = make_album('coldplay', 'a rush of blood to the head')
print(music_3)