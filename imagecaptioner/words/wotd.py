import feedparser
from words.word import Word
from words.wotdparser import WotdParser


class Wotd:
    """Fetches Merriam-Webster's Word of the Day."""

    MW_RSS_FEED_URL = 'https://www.merriam-webster.com/wotd/feed/rss2'

    def wotd(self):
        # TODO (nphair): Parse smarter.
        word = self._feed.entries[0].title
        desc = self._feed.entries[0].description
        parser = WotdParser(word)
        parser.feed(desc)
        if not parser.definition:
            raise RuntimeError('Failed to extract definition for the WOTD.')
        return Word(word, parser.definition)

    def __init__(self):
        self._feed = feedparser.parse(Wotd.MW_RSS_FEED_URL)


