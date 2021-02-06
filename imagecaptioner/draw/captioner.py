from wand.image import Image
from wand.font import Font
from wand.color import Color
from draw.constants import ASPECT_VALUES
from pathlib import Path


class Captioner:
    """Add a caption to an image."""

    DEFAULT_XR = 2.2
    DEFAULT_PADDING = 10
    DEFAULT_FONT_FAMILY = 'roboto'
    DEFAULT_FONT_PATH = '../resources/Roboto/Roboto-Regular.ttf'

    def _calculate_font_size(self, image_height):
        """https://www.md-subs.com/saa-subtitle-font-size"""
        x_height = Captioner.DEFAULT_XR * image_height / 100
        aspect_ratio = ASPECT_VALUES[self._font_family.lower()]
        return x_height / aspect_ratio

    def caption(self, input_filename, output_filename, caption):
        with Image(filename=input_filename) as img:
            with img.clone() as clone:
                font_path = Path(Captioner.DEFAULT_FONT_PATH).resolve().as_posix()
                font_color = Color(self._font_folor)
                if self._best_fit:
                    font = Font(path=font_path, color=font_color, stroke_color=font_color)
                else:
                    font_size = self._calculate_font_size(img.height)
                    font = Font(path=font_path, color=font_color, stroke_color=font_color, size=font_size)
                clone.caption(text=caption, gravity=self._gravity, font=font)
                clone.save(filename=output_filename)

    def __init__(self, font_color, gravity, best_fit):
        # TODO (nphair): Pull image from web.
        self._font_folor = font_color
        self._font_family = Captioner.DEFAULT_FONT_FAMILY
        self._gravity = gravity
        self._best_fit = best_fit
