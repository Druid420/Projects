import requests
from bs4 import BeautifulSoup

#Ask for user input
print('Enter the Word(s) you would like the Definiton(s) for.\nType "done" when you have entered all the words.')

words = []
while True:
    word = input('Enter the Word: ')
    if word == 'done':
      break
    else:
      words.append(word)
      continue


fails = []
for word in words:
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
    #Print results
    print('\n\nWord:', word, '\nPart of Speech:', pos, '\nDefinition:', defin + '.', '\nExample:', examp + '.')
  except:
    #adds failed words to a list of failed words
    fails.append(word)

if len(fails) > 0:
  print("\n\nThe following words were not successful: ")
  for i in fails:
    print(i)