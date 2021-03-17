import json
import difflib

data = json.load(open('data.json'))

def retrieve(word):
	if word.lower() in data.keys():
		return data[word.lower()]
	elif word.upper() in data.keys(): # abbreviations like USA
		return data[word.upper()]
	elif word.capitalize() in data: # names, countries, like America
		return data[word.capitalize()]
	elif len(difflib.get_close_matches(word,data.keys())) > 0:
		possibles = difflib.get_close_matches(word, data.keys(), n=3, cutoff=0.8)
		for suggestion in possibles:
			response = input('Did you mean: {} instead?\n'.format(suggestion))
			if(response.lower() in ['y', 'yes']):
				return data[suggestion]
	return None

print('Welcome to the Thesaurus ...')
while True:
	word = input('Enter a word, or \'q\' to quit: ')
	if(word=='q'):
		break
	else:
		retrieval = retrieve(word)
		if(retrieval):
			for definition in retrieval:
				print('- ' + definition)
		else:
			print('Word not in dictionary')