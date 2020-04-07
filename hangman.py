import bs4
import requests
import csv
import re
import random
from os import path



print("Checking for data file.")
if not path.exists("data.csv"):
    print("Data file not found. Creating...")
    html = requests.get("https://www.hangmanwords.com/words").text
    source = bs4.BeautifulSoup(html,'html.parser')

    with open("data.csv", 'w',newline='') as file:
        words = csv.writer(file)
        for element in source.find('ul',class_='list-cols'):
            for text in element:
                if text != "\n" and ' ' not in text:
                    words.writerow(element)
    print("Data file created\n\n")
else:
    print("Data file found.")

reader = csv.reader(open("data.csv"))
wordList = [i[0] for i in reader]
lives = 5
correct = []
wrong = []

word = wordList[random.randint(0,len(wordList))].upper()
# print(word)
print("""Let's Play Hangman.
A word has been chosen at random.
Your aim is to guess the word. You have a total of 5 chances""")
while lives >= 0:
    for i in word:
        if i in correct:
            print(i,end=' ')
        else:
            print("_",end =' ')
    print("\n")
 
    guess = input(f"""You have {lives} lives.
Your wrong guesses are {wrong}
Guess a Letter(only the first one will be considered): """).upper()[0]

    if guess in word:
        correct.append(guess.upper())
    elif guess not in wrong:
        wrong.append(guess.upper())
        lives -= 1
    
    if sorted(correct) == sorted(list(set(word))):
        print(f"\nCongratulations! The word is {word}. You won!")
        break
    if lives == 0:
        print(f"\nYou ran out of lives!\nThe word was {word}.\nBetter luck next time.")
        break
