from asciiArt import AsciiArt

class MainMenu():

    def __init__(self):
        self.menuOptions = ['Start Game', 'Help', 'Exit Game']
        self.option = 0
        self.graphics = AsciiArt()

    def menuSelect(self):
        isRunning = True
        while isRunning:
            try:
                self.graphics.printSpaceWall()
                userInput = self.graphics.printInputInt("Choose a number: ")
                if userInput < 1 or userInput > 3:
                    raise ValueError
                isRunning = False
            except ValueError: 
                self.graphics.printSpaceWall()
                self.graphics.printBorderLine( "That is not a valid option.")
                
        self.graphics.printUnderLine()
        return userInput



    # ===============
    #  Print Methods
    # ===============

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



    # ==============
    #  Test Methods
    # ==============

    # def countCharacters(self, word: str):
    #     count = 0
    #     for _ in word:
    #         count += 1

    #     return count