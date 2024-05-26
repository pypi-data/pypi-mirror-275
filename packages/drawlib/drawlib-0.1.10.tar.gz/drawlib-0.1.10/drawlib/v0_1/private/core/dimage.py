# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

"""drawlib image class

drawlib depends on ``PIL.Image.Image`` for drawing image.
It is very useful and easy to use.
However, drawlib want to let user handle image **very very** easy.
This module and its class ``Dimage`` achieves it.

"""

from __future__ import annotations

import os
from typing import Union, Tuple, Dict, List, cast
from PIL import (
    Image,
    ImageFilter,
    ImageOps,
    ImageEnhance,
    ImageChops,
)
from drawlib.v0_1.private.util import (
    error_handler,
    get_script_relative_path,
)

list_ = list


class DimageCache:

    def __init__(self):
        self._cache: Dict[str, Dimage] = {}

    def has(self, name: str) -> bool:
        """check whether having Dimage cache or not.

        Args:
            name: cache name

        Returns:
            bool: whether cache exist or not.

        """

        return name in self._cache

    def set(self, name: str, image: Union[str, Dimage, Image.Image]) -> None:
        """Set **copied** Dimage cache with provided name key.

        This method copies original object and set copied one.
        It means you can modify original object after caching.
        It doesn't modify cached object.

        Args:
            name: cache key.
            image: file path or Dimage or PIL image.

        Returns:
            None

        """

        self._cache[name] = Dimage(image=image, copy=True)

    def list(self) -> List[str]:
        return list_(self._cache.keys())

    def get(self, name: str) -> Dimage:
        """Get **copied** Dimage cache via name(key).

        This method doesn't return original object.
        But **copied** object.
        So, you can modify returned Dimage object.
        It doesn't harm original cached Dimage object.

        Args:
            name: cache key.

        Returns:
            Dimage: copy of original cached object.

        """

        if not self.has(name):
            raise ValueError(f'Dimage "{name}" is not cached.')
        return self._cache[name].copy()

    def delete(self, name: str) -> None:
        """Delete Dimage cache

        Delete Dimage cache if exist.
        If not exist, just ignore deletion request.

        Args:
            name: cache key.

        Returns:
            None

        """

        if self.has(name):
            del self._cache[name]


class Dimage:
    """drawlib image class

    Providing very easy methods for read/write and applying effects to image.
    This class is wrapper of ``PIL.Image.Image``.
    So, you can get/set PIL image from this class.
    If you needs apply advanced effects, use PIL Image instead.

    """

    cache = DimageCache()

    @error_handler
    def __init__(
        self,
        image: Union[str, Dimage, Image.Image],
        copy: bool = False,
    ):
        """Initialize Dimage from file, PIL Image, Dimage.

        Initialize Dimage from file path, PIL Image, Dimage.

        Note:
            File path is relative to user code which calls ``Dimage()``.
            Not from where you call python (default path behavior).
            If you want to have normal path behavior,
            convert relative path to absolute path.
            And then, pass to this class.

        """

        # create new PIL.Image instance
        if isinstance(image, str):
            image_str = cast(str, image)  # for mypy check
            image_str = get_script_relative_path(image_str)
            if not os.path.exists(image_str):
                raise FileNotFoundError(f'file "{image_str}" does not exist.')
            self._pilimg = Image.open(image_str)

        elif isinstance(image, Image.Image):
            if copy:
                self._pilimg = image.copy()
            else:
                self._pilimg = image

        elif isinstance(image, Dimage):
            if copy:
                self._pilimg = image._pilimg.copy()
            else:
                self._pilimg = image._pilimg

        else:
            raise ValueError(f'Dimage does not support type "{type(image)}".')

    @error_handler
    def get_pil_image(self) -> Image.Image:
        """Get **copied** PIL Image.

        Get **copied** PIL Image which Dimage instance holds.
        Modification to the PIL Image has no effects to Dimage.

        Returns:
            PIL.Image.Image: copy of PIL Image.

        """

        return self._pilimg.copy()

    @error_handler
    def get_image_size(self) -> Tuple[int, int]:
        width, height = self._pilimg.size
        return (width, height)

    @error_handler
    def copy(self) -> Dimage:
        """Get copied Dimage

        Create another Dimage instance which has same content.

        Returns:
            Dimage: deep copied image

        """

        return Dimage(self)

    @error_handler
    def save(self, file: str) -> None:
        """Save Dimage data to file

        Save to specified file path.
        Path is relative to script file which calls this method.

        Args:
            file: write file path. relative to user script file.

        Returns:
            None

        """

        if not isinstance(file, str):
            raise ValueError('arg "file" must be str.')

        abspath = get_script_relative_path(file)
        directory = os.path.dirname(abspath)
        os.makedirs(directory, exist_ok=True)
        self._pilimg.save(abspath, quality=95)

    """
    @error_handler
    def border(
        self,
        width: int,
        color: Union[Tuple[int, int, int], Tuple[int, int, int, float]],
    ) -> Dimage:
        print(color)

        new_img = ImageOps.expand(
            self._pilimg,
            border=width,
            # pillow supports (R, G, B) and (R, G, B, A)
            fill=(color[0], color[1], color[2]),
        )
        return Dimage(new_img)
    """

    @error_handler
    def _rotate(self, angle: float) -> Dimage:
        """Get rotated new Dimage. Original Dimage is keeped.

        Get new Dimage which has rotated.

        Args:
            angle: between 0.0 ~ 360. pixel size can be changed. New area becomes transparent.

        Returns:
            Dimage: new rotated image.

        """

        newimg = self._pilimg.rotate(
            angle,
            resample=Image.Resampling.BICUBIC,
            expand=True,
        )
        return Dimage(newimg)

    @error_handler
    def resize(self, width: int, height: int) -> Dimage:
        """Get resized new Dimage. Original Dimage is keeped.

        Get new Dimage which has resized.

        Args:
            width: new image width
            height: new image height

        Returns:
            Dimage: new rotated image.

        """

        newimg = self._pilimg.resize(
            (width, height),
            resample=Image.LANCZOS,  # pylint: disable=no-member
        )
        return Dimage(newimg)

    @error_handler
    def flip(self) -> Dimage:
        """Get flipped new Dimage. Original Dimage is keeped.

        Get new Dimage which has flip effect.

        Returns:
            Dimage: new flipped image.

        """

        newimg = ImageOps.flip(self._pilimg)
        return Dimage(newimg)

    @error_handler
    def mirror(self) -> Dimage:
        """Get mirrored new Dimage. Original Dimage is keeped.

        Get new Dimage which has mirror effect.

        Returns:
            Dimage: new mirror image.

        """

        newimg = ImageOps.mirror(self._pilimg)
        return Dimage(newimg)

    @error_handler
    def invert(self) -> Dimage:
        """Get inverted new Dimage. Original Dimage is keeped.

        Get new Dimage which has invert effect.

        Returns:
            Dimage: new inverted image.

        """

        if "A" not in self._pilimg.mode:
            # has no tranceparency. use function
            newimg = ImageOps.invert(self._pilimg)
            return Dimage(newimg)

        # Invert RGB channels
        r, g, b, a = self._pilimg.split()
        r = Image.eval(r, lambda x: 255 - x)
        g = Image.eval(g, lambda x: 255 - x)
        b = Image.eval(b, lambda x: 255 - x)

        # Merge inverted RGB channels with original alpha channel
        inverted_image = Image.merge("RGBA", (r, g, b, a))
        return Dimage(inverted_image)

    @error_handler
    def grayscale(self) -> Dimage:
        """Get grayscaled new Dimage. Original Dimage is keeped.

        Get new Dimage which has grayscale effect.

        Returns:
            Dimage: new grayscaled image.

        """

        newimg = self._pilimg.convert("LA")
        return Dimage(newimg)

    @error_handler
    def brightness(self, brightness_: float = 0.5) -> Dimage:
        """Get brightness changed new Dimage. Original Dimage is keeped.

        Get new Dimage which has change brightness effect.

        Returns:
            Dimage: new brightness changed image.

        """

        enhancer = ImageEnhance.Brightness(self._pilimg)
        newimg = enhancer.enhance(brightness_)
        return Dimage(newimg)

    @error_handler
    def sepia(self) -> Dimage:
        """Get sepia color new Dimage. Original Dimage is keeped.

        Get new Dimage which has sepia effect.

        Returns:
            Dimage: new sepia color image.

        """

        gray = self._pilimg.convert("L")
        sepia_image = Image.merge(
            "RGB",
            (
                gray.point(lambda x: x * 240 / 255),
                gray.point(lambda x: x * 200 / 255),
                gray.point(lambda x: x * 145 / 255),
            ),
        )
        if "A" not in self._pilimg.mode:
            return Dimage(sepia_image)

        # add alpha from original
        alpha_mask = self._pilimg.split()[3]
        sepia_image.putalpha(alpha_mask)
        return Dimage(sepia_image)

    @error_handler
    def colorize(
        self,
        black: Union[str, int],
        white: Union[str, int],
        # black: Union[str, Tuple[int, int, int]],
        # white: Union[str, Tuple[int, int, int]],
    ) -> Dimage:
        """Get colorized new Dimage. Original Dimage is keeped.

        Get new Dimage which has colorize effect.

        Returns:
            Dimage: new colorized image.

        """

        gray = self._pilimg.convert("L")
        colorized_image = ImageOps.colorize(gray, black=black, white=white)
        if "A" not in self._pilimg.mode:
            return Dimage(colorized_image)

        # add alpha from original
        alpha_mask = self._pilimg.split()[3]
        colorized_image.putalpha(alpha_mask)
        return Dimage(colorized_image)

    @error_handler
    def posterize(self, num_colors: int = 4) -> Dimage:
        """Get posterized new Dimage. Original Dimage is keeped.

        Get new Dimage which has posterized effect.

        Returns:
            Dimage: new posterized image.

        """

        if "A" not in self._pilimg.mode:
            newimg = ImageOps.posterize(self._pilimg, num_colors)
            return Dimage(newimg)

        r, g, b, a = self._pilimg.split()
        r = ImageOps.posterize(r, num_colors)
        g = ImageOps.posterize(g, num_colors)
        b = ImageOps.posterize(b, num_colors)
        newimg = Image.merge("RGBA", (r, g, b, a))
        return Dimage(newimg)

    @error_handler
    def mosaic(self) -> Dimage:
        """Get mosiac new Dimage. Original Dimage is keeped.

        Get new Dimage which has mosaic effect.

        Returns:
            Dimage: new mosaic image.

        """

        gimg = self._pilimg.filter(ImageFilter.GaussianBlur(4))
        newimg = gimg.resize(
            (self._pilimg.size[0] // 8, self._pilimg.size[1] // 8),
            # [x // 8 for x in self._pilimg.size],
        ).resize(self._pilimg.size)
        return Dimage(newimg)

    @error_handler
    def blur(self) -> Dimage:
        """Get blur new Dimage. Original Dimage is keeped.

        Get new Dimage which has blur effect.

        Returns:
            Dimage: new blur image.

        """

        newimg = self._pilimg.filter(ImageFilter.BLUR)
        return Dimage(newimg)

    @error_handler
    def line_extraction(self) -> Dimage:
        """Get line extracted new Dimage. Original Dimage is keeped.

        Get new Dimage which has line extraction effect.

        Returns:
            Dimage: new line extracted image.

        """

        gray = self._pilimg.convert("L")
        gray2 = gray.filter(ImageFilter.MaxFilter(5))
        senga_inv = ImageChops.difference(gray, gray2)
        newimg = ImageOps.invert(senga_inv)
        return Dimage(newimg)

    @error_handler
    def remove_margin(
        self,
        margin_color: Union[None, str, Tuple[int, int, int]],
    ) -> Dimage:
        """Get margin removed new Dimage. Original Dimage is keeped.

        Get new Dimage which has margin removed.

        Returns:
            Dimage: new margin removed image.

        """

        if margin_color is None:
            if "A" not in self._pilimg.mode:
                message = "Can't remove transparent margin from RGB image."
                raise ValueError(message)
            crop = self._pilimg.split()[-1].getbbox()
            new_image = self._pilimg.crop(crop)
            return Dimage(new_image)

        raise NotImplementedError("Implement later")
