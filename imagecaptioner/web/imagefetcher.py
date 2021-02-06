import requests
import tempfile


class ImageFetcher:
    """Fetch an image from the web and write to a tempfile."""
    def fetch(self, url):
        r = requests.get(url)
        self._output.write(r.content)
        self._output.flush()
        return self._output.name

    def clean(self):
        self._output.close()

    def __init__(self):
        self._output = tempfile.NamedTemporaryFile()
