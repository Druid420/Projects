import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

class App():
  def __init__(self):
    # Initalizes a blank window the size "650x450"
    self.root = tk.Tk()

    # Sets the window text 
    self.root.title("Definitions WebScrapper")

    # Initalizes the main frame of the window and sets its bg color to "white"
    self.root.configure(bg="white")
        # Style configuration
    style = ttk.Style()
    style.configure("Custom.TFrame", background="white")

    self.mainframe = ttk.Frame(self.root, padding=(3,3,12,12), style="Custom.TFrame")
    self.mainframe.pack(fill="both", expand=True)
    self.frame = ttk.Frame(self.mainframe)
    
    self.title = ttk.Label(self.mainframe, text = "Find Definitions", background = 'white', font =("Times New Roman", 15), anchor = "center")
    
    self.input_words = ttk.Entry(self.mainframe)
    self.words = []
    self.display_text = ""
    self.display_frame = ttk.Frame(self.mainframe, borderwidth=5, relief= "sunken", width=200,height=100)

    self.addword_button = ttk.Button(self.mainframe, text = "Add word", command = self.add_word)
    #self.words_label = ttk.Label(self.mainframe, text = self.display_text)
    self.finddef_button = ttk.Button(self.mainframe, text="Find Definitons", command= self.find_defs)

    self.display_text_widget = Text(self.display_frame, wrap=WORD)
    self.display_text_widget.pack(expand=True, fill='both')
    
    # Bind the Enter key to the add_word function
    self.input_words.bind("<Return>", self.add_word)
    
    self.title.grid(column = 0, row=0, columnspan= 7, sticky= "NWES")
    self.display_frame.grid( column= 0, row = 1, columnspan= 2, rowspan= 2, sticky= 'W')
    self.input_words.grid( column = 3, row = 1, columnspan= 4)
    self.addword_button.grid( column = 3, row = 2, pady = 10, columnspan= 2)
    self.finddef_button.grid(column= 5, row=2, columnspan=2)


    #
    self.root.mainloop()
    return
  

  def add_word(self, event = None):
   
    # Get what word user enters 
    newText = self.input_words.get()
   
    # Append new word to list of words and update display text
    if newText != "" :
      self.words.append(newText)
      if (self.display_text == ""):
        self.display_text += newText
      else: 
        self.display_text += (", "+ newText)
      
      # Clear the Text widget and insert updated text
      self.display_text_widget.delete(1.0, END)
      self.display_text_widget.insert(END, self.display_text)
    
    # Reset user input
    self.input_words.delete(0,"end")

    
    print(self.words)

  def find_defs(self):
    self.display_text = ""
    fails = []
    text = ""
    for word in self.words:
      try:  #Get website's HTML code
        url = (f"https://www.google.com/search?q=define+{word}")
        html = requests.get(url)

        #Interpret HTML code
        soup = BeautifulSoup(html.content, 'html.parser')

        # Search for elements with class 'BNeawe s3v9rd AP7Wnd'
        results_def = soup.find_all('div', class_= 'BNeawe s3v9rd AP7Wnd')

        #Get Part of Speech, Definition, and Example Sentence
        data = results_def[0].text
        split_data = data.split('.')
        p1 = data.split("\n")
        p2 = p1[1]
        p3_def = p2.split('.')
        p3_ex = p2.split('"')
        pos = p1[0]
        defin = p3_def[0]
        examp = p3_ex[1]
        #display results
        self.display_text += ("Word: ", word, ' Part of Speech: ', pos, ' Definition: ', defin)
        print(self.display_text)
        print('go')
      except:
        #adds failed words to a list of failed words
        fails.append(word)

    if len(fails) > 0:
      self.display_text += ("\n\nThe following words were not successful: ")
      for i in fails:
        self.display_text += ("  "+ i)
      self.display_text_widget.delete(1.0,END)
      self.display_text_widget.insert(END, self.display_text)

if __name__ == '__main__':
  App()
