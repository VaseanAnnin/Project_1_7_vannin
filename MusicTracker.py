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

running = True

while running:
    menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        print("Add Song")
    elif user_input == "2":
        print("View Songs")
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
        