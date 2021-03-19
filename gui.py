from tkinter import Tk, Button, Entry, Label, messagebox, StringVar, Text, END
import json
import difflib

def searchBtnCmd():
	result = lookup(entryVal.get())
	text.delete(1.0, END)
	if(result):
		for line in result:
			text.insert(END, '- ' + line + '\n')
	else:
		text.insert(END, 'Sorry - word cannot be found')

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
			response = messagebox.askyesno('Hmmmmm ...', 'Did you mean {}?'.format(suggestion))
			if(response):
				return data[suggestion]
	return None

data = json.load(open('data.json'))

window = Tk()

entryVal = StringVar()
entry = Entry(window, textvariable=entryVal)
entry.pack()

b1 = Button(window, text='Search', command=searchBtnCmd)
b1.pack()

text = Text(window)
text.pack()

qButton = Button(window, text='Quit', command=window.destroy)
qButton.pack()
window.mainloop()