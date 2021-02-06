from draw.captioner import Captioner
from words.wotd import Wotd
import argparse
import time

# TODO (nphair): Sanitize input, check file existence, etc.

parser = argparse.ArgumentParser(description='Caption an image with some text.')
parser.add_argument('filename', help='input image to caption', )
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

captioner = Captioner(args.color, args.gravity, best_fit)
captioner.caption(args.filename, output, caption)
print(f'captioned image written to {output}')

