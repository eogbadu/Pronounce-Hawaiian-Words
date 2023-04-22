# File:           proj1.py
# Author:         Ekele Ogbadu
# Date:           29 MAR 2019
# Section:        09
# E-mail:         eogbadu1@umbc.edu
# Description:    This program takes in a Hawaiian word or phrase and prints
#                 out the correct way to pronounce it.

# Info for getting choice
ANSWERS      = ["y", "yes", "n", "no"]
CONTINUE     = "Do you want to enter another word? (y/yes/n/no): "
QUESTION     = "Enter a Hawaiian phrase to pronounce: "

# Infor about characters and character sounds
OKINA        = "'"
LETTERS      = ["h", "k", "l", "m", "n", "p", "w", "a", "e", "i", "o", "u", "'"]
VOWELS       = ["a", "e", "i", "o", "u"]
VOWEL_SOUND  = ["ah", "eh", "ee", "oh", "oo"]
COMP_VOWELS  = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
COMP_SOUND   = ["eye", "eye", "ow", "ow", "ay", "eh-oo", "ew", "oy", "ow", "ooey"]


##############################################################################
# getHawaiianPhrase() Asks the user to input a Hawaiian phrase,
#                     re-prompting them if the phrase is not valid
#                     (and explaining why that is the case)
# Parameters:         Function takes no input
# Return:             userInput; a string of the user’s chosen Hawaiian phrase

def getHawaiianPhrase():
    GOOD_WORD = False    # Boolean flag
    
    while GOOD_WORD == False:
        GOOD_WORD = True
        index = 0
        index2 = 0
        userInput = input(QUESTION)
        words = userInput.split()
        # Start while loop to check the last letter of every word in phrase
        while index < len(words):
            checkLetter = checkLastLetter(words[index])
            if checkLetter == False:
                GOOD_WORD = False
            index += 1
        # start while loop to check if the word is valid
        while index2 < len(words):
            checkWord = checkWordValidity(words[index2])
            if checkWord == False:
                GOOD_WORD = False
            index2 += 1
    return userInput        

#######################################################################
# checkLastLetter   Determines if the last letter in a word is a vowel
# Parameters:       word;  Takes a string, with no spaces
# Return:           goodLetter; a bool stating whether the last letter
#                               is a vowel or not

def checkLastLetter(word):
    goodLetter = True
    if word[len(word) - 1].lower() not in VOWELS:
        print("The word", word, "does not end in a vowel")
        goodLetter = False

    return goodLetter


#########################################################################
# checkWordValidity   Determines if a word has an invalid character
# Parameters:         word;  Takes a string, with no spaces
# Return:             goodWord; a bool stating whether there is an
#                               invalid character in the word

def checkWordValidity(word):
    index = 0
    goodWord = True
    while index < len(word):
        if word[index].lower() not in LETTERS:
            print ("The letter", word[index], "is not valid")
            goodWord = False
        index += 1
        
    return goodWord

###################################################
# getChoice() prompts and reprompts the user until
#             they select a valid choice
# Parameters: question; a string to be asked
#             options; a list of string options
# Return:     choice; a string chosen by the user

def getChoice(question, options):
    choice = input(question).lower()
    while choice not in options:
        print("Enter y/yes/n/no")
        choice = input(question).lower()
    return choice

######################################################################
# pronounce   Determines how to pronounce an entire phrase
# Parameters: phrase;  Takes a string, possibly with multiple words
# Return:     pronunciation; a string showing how the complete phrase
#                            is pronounced

def pronounce(phrase):
    index = 0
    wordList = phrase.split()
    
    while index < len(wordList):
        wordList[index] = pronounceWord(wordList[index])
        index += 1

    pronunciation = " ".join(wordList)
    return pronunciation


####################################################################
# pronounceWord   Determines how to pronounce a single word
# Parameters:     word;  Takes a string, with no spaces
# Return:         word; a string containing the word's
#                                    pronunciation

def pronounceWord(word):
    index = 0
    vowelIndex = 0
    compIndex = 0
    letterList = []
    finalList = []
    # Start while loop to get the pronunciation for the letter "w"
    while index < len(word):
        if word[index].lower() == "w":
            if index > 0:
                # Call pronounceW to get pronunciation of letter "w"
                letterW = pronounceW(word, index)
                newWord = word[0:index] + letterW + word[index + 1:]
                word = newWord
        index += 1

    # Start while loop to print vowel sounds and hyphen
    while vowelIndex < len(word):
        if word[vowelIndex].lower() in VOWELS:
            if word[vowelIndex:vowelIndex + 2].lower() in COMP_VOWELS:
                pronunciation = complexVowel(word[vowelIndex:vowelIndex + 2])
                letterList.append(pronunciation)
                letterList.append("-")
                vowelIndex += 1
            else:
                pronunciation = simpleVowel(word[vowelIndex])
                letterList.append(pronunciation)
                letterList.append("-")
        else:
            letterList.append(word[vowelIndex])
            
        vowelIndex += 1

    letterList = letterList[0:len(letterList) - 1]
        
    newWords =  ("").join(letterList)
    word = fixOkina(newWords)
        
    return word


######################################################################
# fixOkina   Used to rearrange the order of a word with an OKINA in it
# Parameters:         word;  Takes a string, with no spaces
# Return:             word; a string, the same word it received but
#                           rearranged f it has an Okina in it.

def fixOkina(word):
    index = 0
    while index < len(word):
        if word[index] == OKINA:
            word = word[0:index - 1] + word[index: ]
        index += 1
    return word


##########################################################################
# simpleVowel() Determines how a vowel is pronounced
# Parameters:   letter; a single-character string
# Return:       vowelSound; a string showing how the vowel is pronounced

def simpleVowel(letter):
    index = 0
    while index < len(VOWELS):
        if letter.lower() == VOWELS[index]:
            vowelSound = VOWEL_SOUND[index]
        index += 1
    return vowelSound

######################################################################
# complexVowel() Determines how a complex, two-letter
#                vowel is pronounced
# Parameters:    vowels; a two-character string
# Return:        complexVowelSound; a string showing how the complex
#                                   vowel is pronounced

def complexVowel(vowels):
    index = 0
    while index < len(COMP_VOWELS):
        if vowels.lower() == COMP_VOWELS[index]:
            complexVowelSound = COMP_SOUND[index]
        index += 1

    return complexVowelSound

#######################################################################
# pronounceW() Determines how a “w” should be pronounced
# Parameters:  word; a string with a "w" in it
#              index; the index where the "w" resides
# Return:      wSound; Either “v” or “w” depending on the pronunciation

def pronounceW(word, index):
    if index == 0:
        wSound = "w"
    elif ((word[index - 1].lower() == "o") or (word[index - 1].lower() == "u")):
        wSound = "w"
    else:
        wSound = "v"
    
    return wSound

    
def main():
    SENTINEL = "yes"   
    index = 0
    while ((SENTINEL == "yes") or (SENTINEL == "y")):
        userInput = getHawaiianPhrase()
        pronunciation = pronounce(userInput)
        print("The phrase", userInput.upper(), "is pronounced:")
        print("     ", pronunciation.lower())
        SENTINEL = getChoice(CONTINUE, ANSWERS)

main()
