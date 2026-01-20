import json
import os
import random
print("Let's Hang Man")
def main():
     print("Welcome to hangman would you like to start. (y or n)")
     start = input("-> ").lower()
     if start == "y":
          start = True
          start_game(start)
     else:
          print("ok")
     


if not os.path.exists("words.json"):
    print("No words found.")
    exit()

def start_game(start):
    with open("words.json", "r")as file:
            with open("hangman.json", "r")as file2:
                log = json.load(file)
                log2 = json.load(file2)
                print(json.dumps(log, indent=4))
                print(json.dumps(log2, indent=4))
                print(log2["stages"][6])
                
                # print(log["languages"][random.randint(1,7)])
                strikes = 0
                word = log["languages"][random.randint(0,7)]
                # initialize blanks list so we can reveal letters one at a time
                blanks = ["_"] * len(word)
            while start == True:
                print(word)
                print(len(word))
                # show current blanks
                print("".join(blanks))
                guess = input("Take a guess on the letter (press r to guess the word): ")
                # if the guessed character appears in the word, reveal one occurrence
                if len(guess) == 1 and guess in word:
                    # reveal every index where the letter matches and is still hidden
                    for i, ch in enumerate(word):
                        if ch == guess and blanks[i] == "_":
                            blanks[i] = guess
                elif guess == "r":
                    print("What is the word")
                    final_guess = input()
                    if final_guess == word:
                        print("that is correct")
                        main()
                    else:
                        print("that is wrong")
                else:
                    print("incorrect thats one strike.")
                 
list = [1, 2, 3]
#trying
if __name__ == "__main__":
    main()

