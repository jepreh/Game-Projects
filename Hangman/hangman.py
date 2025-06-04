import random
from difficulty import Difficulty
from asciiArt import AsciiArt

class Hangman():

    def __init__(self, mode: int):
        self.word = ""
        self.wordArray = []
        self.guessedCharacters = set()
        self.graphics = AsciiArt()
        self.mode = Difficulty(mode)
        self.setVariableDifficulty()
        self.attempts = self.wordLength + 5

    # Sets variable values depending on difficulty
    def setVariableDifficulty(self):
        if self.mode.value == 1:
            self.wordLength = 5
            self.characters = ["_"] * self.wordLength
            return
        elif self.mode.value == 2:
            self.wordLength = 7
            self.characters = ["_"] * self.wordLength
            return
        elif self.mode.value == 3:
            self.wordLength = 9
            self.characters = ["_"] * self.wordLength
            return
        
    # Generate a random word based on chosen difficulty
    def generateRandomWord(self):
        if self.mode.value == 1:
            self.word = "FRUIT"
            self.wordToArray()
            
        elif self.mode.value == 2:
            self.word = "CERAMIC"
            self.wordToArray()

        elif self.mode.value == 3:
            self.word = "EXPERTISE"
            self.wordToArray()
        return self.word
    
    # Break up letters into an array
    def wordToArray(self):
        for char in self.word:
            self.wordArray.append(char.upper())
    
    # Get user input, can only be of length 1 string
    def userGuess(self):
        self.graphics.printSpaceWall()
        self.graphics.printSpaceWall()
        self.printGuessWord()

        isRunning = True
        while isRunning:
            try:
                self.graphics.printSpaceWall()
                guessLetter = self.graphics.printInputStr("Guess a letter: ")
                if len(guessLetter) != 1 or guessLetter in ['1','2','3','4','5','6','7','8','9','0']:
                    raise ValueError
                isRunning = False
            except ValueError:
                self.graphics.printUnderLine()
                self.graphics.printSingleBlock("That is not a valid option.")
                self.graphics.printSpaceWall()
                self.printGuessWord()

        guessLetter = guessLetter.upper()
        return guessLetter
    
    # Check the user input to see if it is correct/incorrect
    def checkGuess(self, letter: str):
        index = 0
        duplicateCount = 0
        if letter in self.wordArray:
            for char in self.wordArray:
                if letter == char:
                    self.characters[index] = char.upper()
                    if self.wordLength > 0:
                        if duplicateCount == 0:
                            self.attempts -= 1
                            self.graphics.printUnderLine()
                            self.graphics.printSingleBlock(f"You guessed correct! You have {self.attempts} guesses left.")
                        self.wordLength -= 1
                        self.wordArray[index] = ""
                        index += 1
                        duplicateCount += 1
                        self.guessedCharacters.add(letter)
                    else:
                        self.wordLength -= 1
                        self.attempts -= 1
                        self.guessedCharacters.add(letter)
                else:
                    index += 1
            
        elif letter in self.guessedCharacters: 
            self.graphics.printUnderLine()
            self.graphics.printSingleBlock(f"You have already guessed that. You have {self.attempts} guesses left.")        
        
        else:
            self.attempts -= 1
            self.graphics.printUnderLine()
            if self.attempts > 0:
                self.guessedCharacters.add(letter)
                self.graphics.printSingleBlock(f"Your guess is incorrect. You have {self.attempts} guesses left.")


    # ===============
    #  Print Methods
    # ===============

    # Print start of hangman guessing game
    def printGameStart(self):
        self.graphics.printSingleBlock(f"You have chosen: {self.mode.name}")
        self.graphics.printSingleBlock(f"You have {self.attempts} guesses to guess the word.")

    # Prints the remaining letters left to guess
    def printGuessWord(self):
        remaining = self.printRemainingWord()
        self.graphics.printBorderLine(f"{remaining}")
        return
    
    # Add letters from character list to string with underscores
    def printRemainingWord(self):
        underscores = ""
        count = 0
        border = True
        while border:
            underscores = underscores + " "
            count += 1
            if count == 16:
                border = False
        for _ in self.characters:
            underscores = underscores + _.upper() + "  "
        return underscores
    
    def printFullWord(self):
        self.graphics.printSingleBlock(self.word.upper())

    def printWin(self):
        self.graphics.printSpaceWall()
        self.printGuessWord()
        self.graphics.printSingleBlock("Congratulations!!! You guessed the word.")
        self.graphics.printSpaceWall()
        self.graphics.printBorderLine(f"    It took you {len(self.guessedCharacters)} tries.")
        self.graphics.printUnderLine()

    def printLoss(self):
        self.graphics.printSpaceWall()
        self.printGuessWord()
        self.graphics.printSingleBlock("You failed to guess the word... Better luck next time!")
