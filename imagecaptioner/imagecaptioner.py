from draw.captioner import Captioner
from words.wotd import Wotd
import argparse
import time

# TODO (nphair): Sanitize input, check file existence, etc.

parser = argparse.ArgumentParser(description='Caption an image with some text.')
parser.add_argument('filename', help='input image to caption', )
parser.add_argument('-o', '--output', help='output filename')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--wotd', help='use the MW wotd as the caption', action='store_true')
group.add_argument('-c', '--caption', help='text to use as the caption')
args = parser.parse_args()

caption = str(Wotd().wotd()) if args.wotd else args.caption
output = args.output if args.output else f'{int(time.time())}_{args.filename}'

captioner = Captioner()
captioner.caption(args.filename, output, caption)
print(f'captioned image written to {output}')

