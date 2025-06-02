import msvcrt
import sys

class AsciiArt():

    def __init__(self):
        self.gameWidth = 87

    # Main title screen
    def printTitleScreen(self):
        print(r"""        
______________________________________________________________________________________
|       ___                                                                           |
|      (   )                                                                          |
|       | | .-.     .---.   ___ .-.     .--.    ___ .-. .-.     .---.   ___ .-.       |
|       | |/   \   / .-, \ (   )   \   /    \  (   )   '   \   / .-, \ (   )   \      |
|       |  .-. .  (__) ; |  |  .-. .  ;  ,-. '  |  .-.  .-. ; (__) ; |  |  .-. .      |
|       | |  | |    .'`  |  | |  | |  | |  | |  | |  | |  | |   .'`  |  | |  | |      |
|       | |  | |   / .'| |  | |  | |  | |  | |  | |  | |  | |  / .'| |  | |  | |      |
|       | |  | |  | /  | |  | |  | |  | |  | |  | |  | |  | | | /  | |  | |  | |      |
|       | |  | |  ; |  ; |  | |  | |  | '  | |  | |  | |  | | ; |  ; |  | |  | |      |
|       | |  | |  ' `-'  |  | |  | |  '  `-' |  | |  | |  | | ' `-'  |  | |  | |      |
|      (___)(___)  `._.'_. (___)(___)  `.__. | (___)(___)(___) `._.'_. (___)(___)     |
|                                      ( `-' ;                                        |
|                                       `.__.                                         |
|_____________________________________________________________________________________|""")

    # Horizontal Borders
    def printUnderLine(self):
        print("|_____________________________________________________________________________________|")

    def printDashLine(self):
        print("|------------------------------------------------------------------------------------|\n")

    def printSpaceWall(self):
        print("|                                                                                     |")

    # Print border along with text
    def printBorderLine(self, text: str):
        startLength = 5
        currentLength = 0
        remainingLength = 0

        # Print the starting border
        for index in range(0, 5):
            if index == 0:
                print("|", end='')
                currentLength += 1
            else:
                print(" ", end='')
                currentLength += 1

        # Print the text
        for char in text:
            print(char, end='')
            currentLength += 1

        # Print the back border
        remainingLength = self.gameWidth - currentLength
        for index in range(0, remainingLength):
            if index == remainingLength - 1:
                print("|")
            else:
                print(" ", end='')

    # Print border along with user input
    def printInputInt(self, text: str):
        currentLength = 0
        remainingLength = 0
        userInput = ''

        # Print the starting border
        for index in range(0, 9):
            if index == 0:
                print("|", end='')
                currentLength += 1
            else:
                print(" ", end='')
                currentLength += 1
        
        # Ask for user input
        print(text, end='', flush=True)

        # Capture user input character by character
        while True:
            char = msvcrt.getch()
            if char in [b'\r', b'\n']:  # Enter key
                break
            elif char == b'\x08':   # Backspace key
                if len(userInput) > 0:
                    userInput = userInput[:-1]
                    print('\b \b', end='', flush=True)
            elif char in [b'\x00', b'\xe0']:  # Special keys (arrows, F1–F12)
                msvcrt.getch()  # Discard second byte
            else:
                char = char.decode()
                userInput += char
                print(char, end='', flush=True)

        currentLength = currentLength + len(text) + len(userInput)

        # Print the end border
        remainingLength = self.gameWidth - currentLength
        for index in range(0, remainingLength):
            if index == remainingLength - 1:
                print("|")
            else:
                print(" ", end='')
                
        userInput = int(userInput)
        return userInput

