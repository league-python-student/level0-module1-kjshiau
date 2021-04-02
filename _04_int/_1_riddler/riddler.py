"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    Riddler=simpledialog.askstring(title="Fun Riddles", prompt="There are 70 people in a pool, but 74 heads pop up in the pool. How is the possible? (hint: this is a play on words)")

    if Riddler == "70 FOREHEADS":

        simpledialog.askstring(title=""

