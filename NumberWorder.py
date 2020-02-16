
def Convert_To_Word(num):

    # Create dictionary to compare
    numDict = {"0": "zero",
               "1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine"}

    # Make sure input is not empty string
    # and greater than 0
    if len(num) == 0:
        return "Input cannot be empty"

    # Make sure input is a number
    if not(CheckStringTryParse(num)):
        return "Input is not a number"

    if int(num) < 0:
        return "Input cannot be negative"

    message = ""
    # Loop to print out result via checking key value
    for char in num:
        message += numDict[char] + " "

    return message


def CheckStringTryParse(str):
    try:
        return int(str)
    except ValueError:
        return False


# Test function
userInput = ["1", "12", "-3", "596", "string", ""]
message = "{number}: '{word}'"

for n in userInput:
    print(message.format(number=n, word=Convert_To_Word(n)))
    print()
