import random
from asciiArt import AsciiArt
# from hangman import Hangman
from mainMenu import MainMenu

class main():
    # Print game start graphics
    graphics = AsciiArt()
    graphics.printTitleScreen()
    menu = MainMenu()
    menu.printMenu()

    # Start game process
    userInput = menu.menuSelect()
    
if __name__ == "__main__":
    main()