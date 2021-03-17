from tkinter import Tk, Button, Entry, Label, messagebox, StringVar, Text, END
import json
import difflib

def buttonCmd():
	result = lookup(entryVal.get())
	text.insert(END, result)

def lookup(word):
	if word.lower() in data.keys():
		return data[word.lower()]
	elif word.upper() in data.keys(): # abbreviations like USA
		return data[word.upper()]
	elif word.capitalize() in data: # names, countries, like America
		return data[word.capitalize()]
	elif len(difflib.get_close_matches(word,data.keys())) > 0:
		possibles = difflib.get_close_matches(word, data.keys(), n=3, cutoff=0.8)
		for suggestion in possibles:
			messagebox.askquestion('Hmmmmm ...', 'Did you mean {}?'.format(suggestion))
			if(messagebox == 'yes'):
				return data[suggestion]
				break
	return 'Word could not be found'

data = json.load(open('data.json'))

window = Tk()

l1 = Label(window, text='Enter your word')
l1.grid(row=0, column=0)

l1 = Label(window, text='Result')
l1.grid(row=0, column=2)

entryVal = StringVar()
entry = Entry(window, textvariable=entryVal)
entry.grid(row=2, column=0, rowspan=2)

b1 = Button(window, text='Search', command=buttonCmd)
b1.grid(row=2, column=1, rowspan=2)

text = Text(window, height=1, width=20)
text.grid(row=2, column=2)

window.mainloop()