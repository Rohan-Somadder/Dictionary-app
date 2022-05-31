'''
Class file for representing a word
'''


import requests


class Word():
    '''
    Class to represent a word
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

    def __init__(self, word, LINK) -> None:
        self. word = word
        self.url = LINK + self.word
        self.data = requests.get(self.url).json()

    def word_meanings(self):
        '''
        Returns the word meanings of the words
        '''
        # list comprehension for representing data as -> partofspeech : defination
        # contains 1 meaning for each part of speech
        meanings = {data["partOfSpeech"]: data["definitions"][0]["definition"]
                    for data in self.data[0]["meanings"]}
        print("Meanings : ")
        for part, meaning in meanings.items():
            print(f"{part} -> {meaning}")

    def examples(self):
        '''
        Returns the examples for use of the words
        '''
