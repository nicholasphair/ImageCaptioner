# ImageCaptioner
A simple cli utility to overlay text on images.

Motivated by a want to caption background images for zoom meetings.

# Installation
First, install [ImageMagic for your system][1].
Then, install the python dependencies.
```bash
python -m pip install -r requirements.txt
```

# Usage
```bash
python3 imagecationer/imagecationer.py --wotd -o output.png test/mona_lisa.png
```


[1]: https://imagemagick.org/script/download.php