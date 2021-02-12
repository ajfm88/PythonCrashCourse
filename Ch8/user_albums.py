#Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop

def make_album(artist_name, album_title, tracks=0):
    """Return a dictionary of information about an album"""
    album = {
        'artist': artist_name.title(), 
        'album': album_title.title(),
        }
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease tell me the artist's name: ")
    print("(enter 'q' at any time to quit)")

    art_name = input("Artist's name: ")
    if art_name == 'q':
        break

    print("\nPlease tell me the album's name: ")
    print("(enter 'q' at any time to quit)")

    alb_name = input("Album's name: ")
    if alb_name == 'q':
        break

    album_and_artist = make_album(art_name, alb_name)
    print(f"\n The artist and the album name are: {album_and_artist}.")