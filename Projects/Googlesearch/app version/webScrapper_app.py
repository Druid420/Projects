import tkinter as tk
from tkinter import ttk
from webScrapper_mod import find_defs

class App():
  def __init__(self):
    # Initalizes a blank window the size "650x450"
    self.root = tk.Tk()
    self.root.geometry("650x450")

    # Sets the window text 
    self.root.title("Definitions WebScrapper")

    # Initalizes the main frame of the window and sets its bg color to "white"
    self.mainframe = tk.Frame(self.root, background = "white")
    self.mainframe.pack(fill="both", expand=True)

    # Puts text at the top of the window and sets its bg color, font, and size. Also places it at the very top of the window.
    self.text = ttk.Label(self.mainframe, text = "Find Definitions", background = 'white', font =("Times New Roman", 30), justify = "center")
    self.text.grid(row=0, column = 0)

    #list
    self.words = []

    # Field to enter words
    self.input_words = ttk.Entry(self.mainframe)
    self.input_words.grid(row = 1, column = 0, pady = 10, sticky = "NWES") # <- Sticky  makes it so its the same length as the text above it

    # Adds word button
    self_addword_button = ttk.Button(self.mainframe, text = "Add word", command = self.add_word)
    self_addword_button.grid(row = 1, column = 1, pady = 10)


    # Button to find definitions
    self_text_button = ttk.Button(self.mainframe, text = "Find definitions", command = find_defs(self.words))
    self_text_button.grid(row = 2, column=0,pady=10)

    #
    self.root.mainloop()
    return
  
  def add_word(self):
    # Get what word user enters 
    newText = self.input_words.get()
    # Append new word to list of words
    self.words.append(newText)
    print(self.words)

if __name__ == '__main__':
  App()