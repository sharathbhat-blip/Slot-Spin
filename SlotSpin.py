from random import choice

slot = ["", "", "", "", "", "", "", "", ""]
symbols = ["⭐", "💎", "🔥", "🍉"]
scores = {"⭐": 2, "💎": 3.5, "🔥": 5, "🍉": 6.5}
correctLines = []

def printBoard():
     for i in range(0, 9):
          slot[i] = ""
     for i in range(0, 9):
          if slot[i] == "":
               slot[i] = choice(symbols)
     for i in range(0, 9):
          if (i+1) % 3 == 0:
               print(slot[i])
          else: print(slot[i] + " | ", end="")

def getDeposit():
     while True:
          deposit = input("How much are you going to deposit? $")
          if deposit.isdigit():
               return int(deposit)
          else:
               print("Invalid Deposit. Enter again.")
amount = getDeposit()

def getBet():
     while True:
          bet = input("How much are you going to bet? $")
          if bet.isdigit():
               return int(bet)
          else:
               print("Invalid bet. Enter again.")

def getLines():
     while True:
          lines = input("How many lines would you like to bet on? (1-3): ")
          if lines.isdigit():
               if 1 <= int(lines) <= 3:
                    return int(lines)
               else: print("The lines to bet on must be between 1 and 3.")
          else:
               print("Invalid number of lines. Enter again.")

def checkMatches():
     correctLines.clear()
     string = ""
     for i in range(0, 9, 3):
          if slot[i] == slot[i+1] and slot[i] == slot[i+2]:
               correctLines.append(slot[i])
     for i in range(0, 3):
          if slot[i] == slot[i+3] and slot[i] == slot[i+6]:
               correctLines.append(slot[i])
     if len(correctLines) >= 1:
          for i in correctLines:
               string += i
          print(f"You got {string}")

def calculation(bet, lines):
     global amount
     amount -= bet * lines
     if lines == len(correctLines):
          for logo in correctLines:
               amount += bet * lines * (scores[logo])
     elif len(correctLines) > 0:
          amount += (bet * lines * (scores[logo]))/abs(lines-len(correctLines))


while True:
     if amount != 0:
          print(f"Amount: {amount}")
          userInput = input("Press Enter to spin...(q to quit)")
          if userInput == "":
               b = getBet()
               l = getLines()
               if b * l <= amount:
                    printBoard()
                    checkMatches()
                    calculation(b, l)
               else:
                    print(f"You dont have ${b*l} in your account!")
                    continue
          elif userInput == "q":
               break
     else:
          print("You are out of balance!")
          break
