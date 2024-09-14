import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score

def welcome(name):
    message = (f"Hello {name} and welcome to the World of Games (WoG).\n"
               f"Here you can find many cool games to play.")
    print(message)

def load_game():
    message = ("Please choose a game to play:\n"
               "1. Memory Game - a sequence of numbers will appear for 1 second\nand you have to guess it back\n"
               "2. Guess Game - guess a number and see if you chose like the computer\n"
               "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    print(message)
    gameNumber = input("Choose a game (1 to 3) >")
    while not gameNumber.isnumeric():
        gameNumber = input("Please input a number >")
    gameNumber = int(gameNumber)
    while((gameNumber < 1) or (gameNumber > 3)):
        gameNumber = int(input("invalid input, please choose a number between 1 and 3 (inclusive) >"))


    difficulty = input("Please choose game difficulty from 1 to 5 >")
    while not difficulty.isnumeric():
        difficulty = input("Please input a number >")
    difficulty = int(difficulty)
    while((difficulty < 1) or (difficulty > 5)):
        difficulty = int(input("invalid input, please choose a number between 1 and 5 (inclusive) >"))

    if(gameNumber == 1):
        shouldSetScore = MemoryGame.play(difficulty)
    elif(gameNumber == 2):
        shouldSetScore = GuessGame.play(difficulty)
    else:
        shouldSetScore = CurrencyRouletteGame.play(difficulty)
    if shouldSetScore == True:
        Score.add_score(difficulty)