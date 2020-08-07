#TIP: use random.randint to get a random word from the list
import random
from os import read


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    #dest = "/home/wtc/problems/submission_001-hangman/short_words.txt"
    my_file =open(file_name,"r")
    words = my_file.readlines()   
    
    return words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    rand_word  =random.randint(0,len(words)-1)
    word = words[rand_word]

    missing_letter = random.randint(0,len(word)-2)
    letter = list(word)
    letter[missing_letter] = '_'
    print("Guess the word: " + ''.join(letter))

    return word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    guess = input("Guess the missing letter: ")
     
    return guess


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)
    #print(words)


if __name__ == "__main__":
    run_game('short_words.txt')

