import sys
import time

from GuessGame import generate_number

def generate_sequence(difficulty):
    myList = []
    for i in range(difficulty):
        myList.append(generate_number(101))
    print(myList)
    time.sleep(1)
    for i in range(101):
        print("\n")
    # sys.stdout.write('\r' + ' ' * len(myList) + '\r')  # Clear the message
    # sys.stdout.flush()
    return myList

def get_list_from_user(difficulty):
    myList = []
    for i in range(difficulty):
        myList.append(int(input(f"Enter number of index {i+1} out of {difficulty} in list: ")))

    return myList

def is_list_equal(userList, gameList):
    for i in range(len(gameList)):
        if gameList[i] != userList[i]:
            print("Wrong!")
            return False

    print("Success")
    return True

def play(difficulty):
    gameList = generate_sequence(difficulty)
    userList = get_list_from_user(difficulty)
    return is_list_equal(userList, gameList)