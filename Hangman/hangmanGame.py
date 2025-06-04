from asciiArt import AsciiArt
from hangman import Hangman
from mainMenu import MainMenu

class main():
    # Print game start graphics
    graphics = AsciiArt()
    menu = MainMenu()

    # Start game process
    # hangmanRunning = True
    # while hangmanRunning:
    graphics.printTitleScreen()
    menu.printMenu()
    userInput = menu.menuSelect()
    if userInput == 1:
        difficulty = menu.menuStartGame()
        hangman = Hangman(difficulty)
        hangman.generateRandomWord()
        hangman.printGameStart()

        # Game loop
        gameRunning = True
        while gameRunning:
            userGuess = hangman.userGuess()
            hangman.checkGuess(userGuess)
            if hangman.wordLength <= 0:
                hangman.printWin()
                gameRunning = False
            
            elif hangman.attempts <= 0:
                hangman.printLoss()
                gameRunning = False

    elif userInput == 2:
        menu.menuHelp()
        hangmanRunning = False
    else:
        menu.exitGame()
        hangmanRunning = False

if __name__ == "__main__":
    main()