from html.parser import HTMLParser


class WotdParser(HTMLParser):
    """A naive parser to try and extract the words-of-the-day definition."""

    PRONUNCIATION_MAGIC = '•'

    def _is_definition(self, data):
        """Assume 3 or more words that do not contain the pronunciation magic is the definition."""
        if WotdParser.PRONUNCIATION_MAGIC in data:
            return False
        return len(data.split()) > 2

    def handle_data(self, data):
        if not self._def_found and data == self._word:
            self._search_active = True
        elif self._search_active and not self._def_found and self._is_definition(data):
            self._definition = data
            self._search_active = False
            self._def_found = True

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self):
        pass

    def __init__(self, word):
        super().__init__()
        self._word = word
        self._definition = None
        # Begin searching only once we've seen the wotd.
        self._search_active = False
        self._def_found = False
