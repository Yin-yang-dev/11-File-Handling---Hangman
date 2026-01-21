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
          exit()
     


if not os.path.exists("words.json"):
    print("No words found.")
    exit()

def start_game(start):
    with open("words.json", "r")as file:
            with open("hangman.json", "r")as file2:
                log = json.load(file)
                log2 = json.load(file2)
                # print(log["languages"][random.randint(1,7)])
                word = log["languages"][random.randint(0,10)]
                # initialize blanks list so we can reveal letters one at a time
                blanks = ["_"] * len(word)
                strikes = 0
            while start == True:
                print(log2["stages"][strikes])
                if strikes == 6:
                        print("You couldn't guess the word.")
                        main()
                # show current blanks
                print("".join(blanks))
                guess = input("Take a guess on the letter (press 1 to guess the word): ")
                # if the guessed character appears in the word, reveal one occurrence
                if len(guess) == 1 and guess in word:
                    # reveal every index where the letter matches and is still hidden
                    for i, ch in enumerate(word):
                        if ch == guess and blanks[i] == "_":
                            blanks[i] = guess
                elif guess == "1":
                    print("What is the word")
                    final_guess = input()
                    if final_guess == word:
                        print("that is correct")
                        main()
                    else:
                        print("that is wrong")
                        print(f"The word was {word}")
                        main()
                else:
                    print("incorrect thats one strike.")
                    strikes += 1
                    

                 
list = [1, 2, 3]
#trying
if __name__ == "__main__":
    main()

