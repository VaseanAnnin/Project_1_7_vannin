"""
Program: Music Collection and Practice Tracker

Author: Vasean Annin

Purpose: This aplication will store and manage the users
music collection as well as track their progress as they practice
the songs in the collection

Date: 06/24/2026

"""

songs = [
    {
    "title": "Freudian",
    "artist": "Daniel Caesar",
    "instrument":"Guitar",
    "genre": "Neo Soul",
    "progress": 79
    }
]

def menu():
    ## This function is for the main menu
    print("\n=====================================")
    print("1. Add Song")
    print("2. View Songs")
    print("3. Search Song")
    print("4. Update Progress")
    print("5. Delete Song")
    print("6. View Statistics")
    print("7. Exit")

def add_song():
    ## This function is for adding a new song
    title = input("Song title: ")
    artist= input("Artists: ")
    instrument = input("Instruments: ")
    genre = input("Genre: ")
    progress = int(input("Progress: "))

    song = {
        "title": title,
        "artist": artist,
        "instrument": instrument,
        "genre": genre,
        "progress": progress
    }
    songs.append(song)

    print("=========Song added=========")

def view_songs():
    ##This function displays the current songs within the app

    if(len(songs)) == 0:
        print("No songs in database")
        return
    
    for i, song in enumerate(songs, start = 1):
        print(f"\nSong {i}")
        print(f"title: {song['title']}")
        print(f"artist: {song['artist']}")
        print(f"instrument: {song['instrument']}")
        print(f"genre: {song['genre']}")
        print(f"progress: {song['progress']}%")


running = True

while running:
    menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_song()
    elif user_input == "2":
        view_songs()
    elif user_input == "3":
        print("Search Song")
    elif user_input == "4":
        print("Update Progress")
    elif user_input =="5":
        print("Delete Song")
    elif user_input == "6":
        print("Statistics")
    elif user_input == "7":
        print ("Keep practicing see you soon!")
        running = False
    
    else:
        print("Selection not recognized please try again")
