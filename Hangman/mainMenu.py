from asciiArt import AsciiArt
from difficulty import Difficulty

class MainMenu():

    def __init__(self):
        self.menuOptions = ['Start Game', 'Help', 'Exit Game']
        self.option = 0
        self.graphics = AsciiArt()
        self.difficultyOption = Difficulty

    # Main menu screen, user selects option 1-3
    def menuSelect(self):
        userInput = self.valueErrorCheck("Choose a number: ", len(self.menuOptions))
        self.graphics.printUnderLine()
        return userInput

    # Start game menu, user selects a difficulty option
    def menuStartGame(self):
        self.graphics.printSingleBlock("START GAME")
        self.printStartMenu()
        userInput = self.valueErrorCheck("Select a difficulty: ", len(self.difficultyOption))
        self.graphics.printUnderLine()
        return userInput
        
    # Outputs a help menu or document (README)
    def menuHelp(self):
        self.graphics.printSingleBlock("Help Menu")
        return
    
    def exitGame(self):
        self.graphics.printSingleBlock("Exiting Game")
        exit()

    # Check user input for value error
    def valueErrorCheck(self, optionText: str, maxOption: int):
        isRunning = True
        while isRunning:
            try:
                self.graphics.printSpaceWall()
                userInput = self.graphics.printInputInt(optionText)
                if userInput < 1 or userInput > maxOption:
                    raise ValueError
                isRunning = False
            except ValueError: 
                self.graphics.printSpaceWall()
                self.graphics.printBorderLine("    That is not a valid option.")
        return userInput


    # ===============
    #  Print Methods
    # ===============

    # Prints the main menu screen
    def printMenu(self):
        count = 1
        self.graphics.printSpaceWall()
        self.graphics.printBorderLine("Main Menu")
        self.graphics.printUnderLine()
        self.graphics.printSpaceWall()
        for option in self.menuOptions:
            self.graphics.printBorderLine(f"    {count}) {option}")
            count += 1
        self.graphics.printUnderLine()

    # Prints the start menu screen with difficulties
    def printStartMenu(self):
        self.graphics.printSpaceWall()
        for option in Difficulty:
            self.graphics.printBorderLine(f"    {option.value}) {option.name}")
        return


    # ==============
    #  Test Methods
    # ==============

    # Count the number of characters in a string
    # def countCharacters(self, word: str):
    #     count = 0
    #     for _ in word:
    #         count += 1

    #     return count