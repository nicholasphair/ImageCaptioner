from draw.captioner import Captioner
from web.imagefetcher import ImageFetcher
from words.wotd import Wotd
import argparse
import time
import re

# TODO (nphair): Sanitize input, check file existence, etc.


# Credit to https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
def is_url(filename):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    return re.match(regex, filename) is not None


parser = argparse.ArgumentParser(description='Caption an image with some text.')
parser.add_argument('filename', help='absolute path or url to an image', )
parser.add_argument('-o', '--output', help='output filename')
parser.add_argument('--color', help='font color', default='#000000')
parser.add_argument('--best-fit', help='adjust the size of the font so as to best fill the size of the image', action='store_true')
caption_group = parser.add_mutually_exclusive_group(required=True)
caption_group.add_argument('--wotd', help='use the MW wotd as the caption', action='store_true')
caption_group.add_argument('-c', '--caption', help='text to use as the caption')
position_group = parser.add_mutually_exclusive_group(required=True)
position_group.add_argument('--top', help='position the caption at the top of the image', action='store_const', const='north', dest='gravity')
position_group.add_argument('--bottom',  help='position the caption at the bottom of the image', action='store_const', const='south', dest='gravity')
position_group.add_argument('--center',  help='position the caption at the center of the image', action='store_const', const='center', dest='gravity')
args = parser.parse_args()

caption = str(Wotd().wotd()) if args.wotd else args.caption
output = args.output if args.output else f'{int(time.time())}_{args.filename}'
best_fit = args.best_fit or args.wotd

is_url = is_url(args.filename)
if is_url:
    image_fetcher = ImageFetcher()
    image = image_fetcher.fetch(args.filename)
else:
    image = args.filename

captioner = Captioner(args.color, args.gravity, best_fit)
captioner.caption(image, output, caption)
print(f'captioned image written to {output}')

