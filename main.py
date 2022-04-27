'''
Dictionary App
API used - Free Dictionary API
Link - https://dictionaryapi.dev/

#TODO : None
'''

import requests

LINK = 'https://api.dictionaryapi.dev/api/v2/entries/en/'


class Word():
    '''
    Class to represent a player
    ...
    Attributes
    ----------
    word : str
        word to search for in the dictionary
    url : str
        url for the get request
    data : json
        data recieved from the get request in jsonified format
    ...
    Methods
    -------
    word_meanings():
        Returns the meanings of the word in different parts of speech.
    examples():
        Returns the different uses of the word in various sentences.
    pronunciation():
        Plays the pronunciation of the word
    '''

    def __init__(self, word) -> None:
        self. word = word
        self.url = LINK + self.word
        self.data = requests.get(self.url).json()

    def word_meanings(self):
        '''
        Returns the word meanings of the words
        '''
        meaning = self.data["meanings"]
        meanings = list(meaning['definitions']['definition'])
        print(" Meanings : ")
        for i, m in enumerate(meanings):
            print(f"{i}.   {m}")

    def examples(self):
        '''
        Returns the meanings of the words
        '''
        pass
