
class Word:
    """A word and definition pair."""

    @property
    def word(self):
        return self._word

    @property
    def definition(self):
        return self._definition

    @word.setter
    def word(self, word):
        print('Be careful not to get your words and definition out of sync!')
        self._word = word

    @definition.setter
    def definition(self, definition):
        print('Be careful not to get your words and definition out of sync!')
        self._definition = definition

    def __str__(self):
        return f'{self._word}: {self._definition}'

    def __init__(self, word, definition):
        self._word = word
        self._definition = definition
