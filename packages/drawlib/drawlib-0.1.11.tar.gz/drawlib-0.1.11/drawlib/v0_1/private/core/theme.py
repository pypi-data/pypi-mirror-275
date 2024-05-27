# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

"""Drawlib style theme

Define style theme at class ``Theme``.
Default or choosed theme is applied if style is not provided.
Instance ``dtheme``  is provided to user to control theme.

"""

from __future__ import annotations
import dataclasses
from typing import Optional, Dict, Tuple, Union, Literal, List
from copy import deepcopy

from drawlib.v0_1.private.util import error_handler
from drawlib.v0_1.private.core.model import (
    IconStyle,
    ImageStyle,
    LineStyle,
    LineArrowStyle,
    ShapeStyle,
    ShapeTextStyle,
    TextStyle,
)
from drawlib.v0_1.private.core.fonts import FontSourceCode
from drawlib.v0_1.private.core.theme_styles import (
    ThemeColors,
    BackgroundColors,
    SourceCodeFonts,
    IconStyles,
    ImageStyles,
    LineStyles,
    LineArrowStyles,
    ShapeStyles,
    ShapeTextStyles,
    TextStyles,
    # Patch Styles
    ArcStyles,
    ArcTextStyles,
    CircleStyles,
    CircleTextStyles,
    DonutsStyles,
    DonutsTextStyles,
    EllipseStyles,
    EllipseTextStyles,
    FanStyles,
    FanTextStyles,
    PolygonStyles,
    PolygonTextStyles,
    RectangleStyles,
    RectangleTextStyles,
    RegularpolygonStyles,
    RegularpolygonTextStyles,
    WedgeStyles,
    WedgeTextStyles,
    # Original arrows
    ArrowStyles,
    ArrowTextStyles,
    # Original polygons
    ChevronStyles,
    ChevronTextStyles,
    ParallelogramStyles,
    ParallelogramTextStyles,
    RhombusStyles,
    RhombusTextStyles,
    StarStyles,
    StarTextStyles,
    TrapezoidStyles,
    TrapezoidTextStyles,
    TriangleStyles,
    TriangleTextStyles,
    # Smart art
    BubblespeechStyles,
    BubblespeechTextStyles,
)
import drawlib.v0_1.private.core.theme_officials as theme_officials


class Theme:
    """Drawlib Thema control class.

    * define theme here
    * provide theme access methods

    """

    @dataclasses.dataclass
    class ThemeStyle:
        # mandatory for default
        backgroundcolor: Union[Tuple[int, int, int], Tuple[int, int, int, float], None] = None
        sourcecodefont: Optional[FontSourceCode] = None
        iconstyle: Optional[IconStyle] = None
        imagestyle: Optional[ImageStyle] = None
        linestyle: Optional[LineStyle] = None
        linearrowstyle: Optional[LineArrowStyle] = None
        shapestyle: Optional[ShapeStyle] = None
        shapetextstyle: Optional[ShapeTextStyle] = None
        textstyle: Optional[TextStyle] = None

        # optional for default
        arcstyle: Optional[ShapeStyle] = None
        arttextstyle: Optional[ShapeTextStyle] = None

    @error_handler
    def __init__(self):
        self._style_names: List[str] = []

        self.colors = ThemeColors()
        self.backgroundcolors = BackgroundColors()
        self.sourcecodefonts = SourceCodeFonts()
        self.iconstyles = IconStyles()
        self.imagestyles = ImageStyles()
        self.linestyles = LineStyles()
        self.linearrowstyles = LineArrowStyles()
        self.shapestyles = ShapeStyles()
        self.shapetextstyles = ShapeTextStyles()
        self.textstyles = TextStyles()

        # patchs
        self.arcstyles = ArcStyles(self.shapestyles)
        self.arctextstyles = ArcTextStyles(self.shapetextstyles)
        self.circlestyles = CircleStyles(self.shapestyles)
        self.circletextstyles = CircleTextStyles(self.shapetextstyles)
        self.donutsstyles = DonutsStyles(self.shapestyles)
        self.donutstextstyles = DonutsTextStyles(self.shapetextstyles)
        self.ellipsestyles = EllipseStyles(self.shapestyles)
        self.ellipsetextstyles = EllipseTextStyles(self.shapetextstyles)
        self.fanstyles = FanStyles(self.shapestyles)
        self.fantextstyles = FanTextStyles(self.shapetextstyles)
        self.polygonstyles = PolygonStyles(self.shapestyles)
        self.polygontextstyles = PolygonTextStyles(self.shapetextstyles)
        self.rectanglestyles = RectangleStyles(self.shapestyles)
        self.rectangletextstyles = RectangleTextStyles(self.shapetextstyles)
        self.regularpolygonstyles = RegularpolygonStyles(self.shapestyles)
        self.regularpolygontextstyles = RegularpolygonTextStyles(self.shapetextstyles)
        self.wedgestyles = WedgeStyles(self.shapestyles)
        self.wedgetextstyles = WedgeTextStyles(self.shapetextstyles)

        # original arrows
        self.arrowstyles = ArrowStyles(self.shapestyles)
        self.arrowtextstyles = ArrowTextStyles(self.shapetextstyles)

        # original polygons
        self.chevronstyles = ChevronStyles(self.shapestyles)
        self.chevrontextstyles = ChevronTextStyles(self.shapetextstyles)
        self.parallelogramstyles = ParallelogramStyles(self.shapestyles)
        self.parallelogramtextstyles = ParallelogramTextStyles(self.shapetextstyles)
        self.rhombusstyles = RhombusStyles(self.shapestyles)
        self.rhombustextstyles = RhombusTextStyles(self.shapetextstyles)
        self.starstyles = StarStyles(self.shapestyles)
        self.startextstyles = StarTextStyles(self.shapetextstyles)
        self.trapezoidstyles = TrapezoidStyles(self.shapestyles)
        self.trapezoidtextstyles = TrapezoidTextStyles(self.shapetextstyles)
        self.trianglestyles = TriangleStyles(self.shapestyles)
        self.triangletextstyles = TriangleTextStyles(self.shapetextstyles)

        # smart art
        self.bubblespeechstyles = BubblespeechStyles(self.shapestyles)
        self.bubblespeechtextstyles = BubblespeechTextStyles(self.shapetextstyles)

        self.apply_official_theme("default")

    #############
    ### Thema ###
    #############

    @error_handler
    def _initialize(self) -> None:
        """Initialize theme.

        This method need to be called before setting manual theme.

        Returns:
            None

        """

        self._style_names: List[str] = []

        self.colors = ThemeColors()
        self.backgroundcolors = BackgroundColors()
        self.sourcecodefonts = SourceCodeFonts()
        self.iconstyles = IconStyles()
        self.imagestyles = ImageStyles()
        self.linestyles = LineStyles()
        self.linearrowstyles = LineArrowStyles()
        self.shapestyles = ShapeStyles()
        self.shapetextstyles = ShapeTextStyles()
        self.textstyles = TextStyles()

        # patchs
        self.arcstyles = ArcStyles(self.shapestyles)
        self.arctextstyles = ArcTextStyles(self.shapetextstyles)
        self.circlestyles = CircleStyles(self.shapestyles)
        self.circletextstyles = CircleTextStyles(self.shapetextstyles)
        self.donutsstyles = DonutsStyles(self.shapestyles)
        self.donutstextstyles = DonutsTextStyles(self.shapetextstyles)
        self.ellipsestyles = EllipseStyles(self.shapestyles)
        self.ellipsetextstyles = EllipseTextStyles(self.shapetextstyles)
        self.fanstyles = FanStyles(self.shapestyles)
        self.fantextstyles = FanTextStyles(self.shapetextstyles)
        self.polygonstyles = PolygonStyles(self.shapestyles)
        self.polygontextstyles = PolygonTextStyles(self.shapetextstyles)
        self.rectanglestyles = RectangleStyles(self.shapestyles)
        self.rectangletextstyles = RectangleTextStyles(self.shapetextstyles)
        self.regularpolygonstyles = RegularpolygonStyles(self.shapestyles)
        self.regularpolygontextstyles = RegularpolygonTextStyles(self.shapetextstyles)
        self.wedgestyles = WedgeStyles(self.shapestyles)
        self.wedgetextstyles = WedgeTextStyles(self.shapetextstyles)

        # original arrows
        self.arrowstyles = ArrowStyles(self.shapestyles)
        self.arrowtextstyles = ArrowTextStyles(self.shapetextstyles)

        # original polygons
        self.chevronstyles = ChevronStyles(self.shapestyles)
        self.chevrontextstyles = ChevronTextStyles(self.shapetextstyles)
        self.parallelogramstyles = ParallelogramStyles(self.shapestyles)
        self.parallelogramtextstyles = ParallelogramTextStyles(self.shapetextstyles)
        self.rhombusstyles = RhombusStyles(self.shapestyles)
        self.rhombustextstyles = RhombusTextStyles(self.shapetextstyles)
        self.starstyles = StarStyles(self.shapestyles)
        self.startextstyles = StarTextStyles(self.shapetextstyles)
        self.trapezoidstyles = TrapezoidStyles(self.shapestyles)
        self.trapezoidtextstyles = TrapezoidTextStyles(self.shapetextstyles)
        self.trianglestyles = TriangleStyles(self.shapestyles)
        self.triangletextstyles = TriangleTextStyles(self.shapetextstyles)

        # smart art
        self.bubblespeechstyles = BubblespeechStyles(self.shapestyles)
        self.bubblespeechtextstyles = BubblespeechTextStyles(self.shapetextstyles)

    @error_handler
    def list_official_themes(self) -> List[str]:
        return ["default", "gray"]

    @error_handler
    def apply_official_theme(self, name: Literal["default", "flat", "black_and_white", "gray"]) -> None:
        if name == "default":
            t = theme_officials.get_default()
        elif name == "flat":
            t = theme_officials.get_flat()
        elif name == "black_and_white":
            t = theme_officials.get_black_and_white()
        elif name == "gray":
            t = theme_officials.get_gray()
        else:
            raise ValueError(f'Theme "{name}" is not supported.')

        default_style = Theme.ThemeStyle(
            backgroundcolor=t.backgroundcolor,
            sourcecodefont=t.sourcecodefont,
            iconstyle=t.iconstyle,
            imagestyle=t.imagestyle,
            linestyle=t.linestyle,
            linearrowstyle=t.linearrowstyle,
            shapestyle=t.shapestyle,
            shapetextstyle=t.shapetextstyle,
            textstyle=t.textstyle,
        )

        named_styles: List[Tuple[str, Theme.ThemeStyle]] = []
        for name, styles in t.named_styles:
            named_style = Theme.ThemeStyle()
            for style in styles:
                if isinstance(style, IconStyle):
                    named_style.iconstyle = style
                elif isinstance(style, ImageStyle):
                    named_style.imagestyle = style
                elif isinstance(style, LineStyle):
                    named_style.linestyle = style
                elif isinstance(style, LineArrowStyle):
                    named_style.linearrowstyle = style
                elif isinstance(style, ShapeStyle):
                    named_style.shapestyle = style
                elif isinstance(style, ShapeTextStyle):
                    named_style.shapetextstyle = style
                elif isinstance(style, TextStyle):
                    named_style.textstyle = style
                else:
                    raise ValueError(f"Unexpected library error. style type is {type(style)}")

            named_styles.append((name, named_style))

        self.apply_custome_theme(
            default_style=default_style,
            named_styles=named_styles,
            theme_colors=t.theme_colors,
        )

    @error_handler
    def apply_custome_theme(
        self,
        default_style: Theme.ThemeStyle,
        named_styles: List[
            Tuple[
                str,
                Theme.ThemeStyle,
            ]
        ] = [],
        theme_colors: List[Tuple[str, Union[Tuple[int, int, int], Tuple[int, int, int, float]]]] = [],
    ) -> None:

        # initialize
        self._initialize()

        self._style_names.append("")

        # set default background color
        _check_color(
            default_style.backgroundcolor,
            "default_style.backgroundcolor is mandatory. "
            "Format is (R, G, B) or (R, G, B, A). Where R,G,B is 0~255 and A is 0.0~1.0.",
        )
        self.backgroundcolors.set(default_style.backgroundcolor)

        # set default soucecode font
        if not isinstance(default_style.sourcecodefont, FontSourceCode):
            raise ValueError("default_style.sourcecodefont is mandatory. Type must be FontSourceCode.")
        self.sourcecodefonts.set(default_style.sourcecodefont)

        # set default styles
        if not isinstance(default_style.iconstyle, IconStyle):
            raise ValueError("default_style.iconstyle is mandatory. Type must be IconStyle.")
        self.iconstyles.set(default_style.iconstyle)

        if not isinstance(default_style.imagestyle, ImageStyle):
            raise ValueError("default_style.imagestyle is mandatory. Type must be ImageStyle.")
        self.imagestyles.set(default_style.imagestyle)

        if not isinstance(default_style.linestyle, LineStyle):
            raise ValueError("default_style.linestyle is mandatory. Type must be LineStyle.")
        self.linestyles.set(default_style.linestyle)

        if not isinstance(default_style.linearrowstyle, LineArrowStyle):
            raise ValueError("default_style.linearrowstyle is mandatory. Type must be LineArrowStyle.")
        self.linearrowstyles.set(default_style.linearrowstyle)

        if not isinstance(default_style.shapestyle, ShapeStyle):
            raise ValueError("default_style.shapestyle is mandatory. Type must be ShapeStyle.")
        self.shapestyles.set(default_style.shapestyle)

        if not isinstance(default_style.shapetextstyle, ShapeTextStyle):
            raise ValueError("default_style.shapetextstyle is mandatory. Type must be ShapeTextStyle.")
        self.shapetextstyles.set(default_style.shapetextstyle)

        if not isinstance(default_style.textstyle, TextStyle):
            raise ValueError("default_style.textstyle is mandatory. Type must be TextStyle.")
        self.textstyles.set(default_style.textstyle)

        # named styles
        for name, styles in named_styles:
            self._style_names.append(name)

            if styles.backgroundcolor is not None:
                _check_color(
                    styles.backgroundcolor,
                    f"name={name}, ThemeStyle.backgroundcolor format must be (R,G,B) or (R,G,B,A). "
                    "Format is (R, G, B) or (R, G, B, A). Where R,G,B is 0~255 and A is 0.0~1.0.",
                )
                self.backgroundcolors.set(styles.backgroundcolor, name)

            if styles.sourcecodefont is not None:
                if not isinstance(styles.sourcecodefont, FontSourceCode):
                    raise ValueError(f"name={name}, ThemeStyle.sourcecodefont type must be FontSourceCode.")
                self.sourcecodefonts.set(styles.sourcecodefont, name)

            if styles.iconstyle is not None:
                if not isinstance(styles.iconstyle, IconStyle):
                    raise ValueError(f"name={name}, ThemeStyle.iconstyle type must be IconStyle.")
                self.iconstyles.set(styles.iconstyle, name)

            if styles.imagestyle is not None:
                if not isinstance(styles.imagestyle, ImageStyle):
                    raise ValueError(f"name={name}, ThemeStyle.imagestyle type must be ImageStyle.")
                self.imagestyles.set(styles.imagestyle, name)

            if styles.linestyle is not None:
                if not isinstance(styles.linestyle, LineStyle):
                    raise ValueError(f"name={name}, ThemeStyle.linestyle type must be LineStyle.")
                self.linestyles.set(styles.linestyle, name)

            if styles.linearrowstyle is not None:
                if not isinstance(styles.linearrowstyle, LineArrowStyle):
                    raise ValueError(f"name={name}, ThemeStyle.linearrowstyle type must be LineArrowStyle.")
                self.linearrowstyles.set(styles.linearrowstyle, name)

            if styles.shapestyle is not None:
                if not isinstance(styles.shapestyle, ShapeStyle):
                    raise ValueError(f"name={name}, ThemeStyle.shapestyle type must be ShapeStyle.")
                self.shapestyles.set(styles.shapestyle, name)

            if styles.shapetextstyle is not None:
                if not isinstance(styles.shapetextstyle, ShapeTextStyle):
                    raise ValueError(f"name={name}, ThemeStyle.shapetextstyle type must be ShapeTextStyle.")
                self.shapetextstyles.set(styles.shapetextstyle, name)

            if styles.textstyle is not None:
                if not isinstance(styles.textstyle, TextStyle):
                    raise ValueError(f"name={name}, ThemeStyle.textstyle type must be TextStyle.")
                self.textstyles.set(styles.textstyle, name)

        for t in theme_colors:
            if not isinstance(t, tuple):
                raise ValueError()
            if len(t) != 2:
                raise ValueError()

            name, theme_color = t
            if not isinstance(name, str):
                raise ValueError()
            _check_color(
                theme_color,
                f"name={name}, ThemeStyle.themecolors format must be (R,G,B) or (R,G,B,A). "
                "Format is (R, G, B) or (R, G, B, A). Where R,G,B is 0~255 and A is 0.0~1.0.",
            )

            self.colors.set(theme_color, name)

    @error_handler
    def print_theme_colors(self) -> None:
        print(self._get_theme_colors())

    def _get_theme_colors(self) -> str:
        max_len = 0
        for name in self.colors.list():
            if len(name) > max_len:
                max_len = len(name)

        lines = []
        for name in self.colors.list():
            c = self.colors.get(name)
            c0 = str(c[0]).rjust(3)
            c1 = str(c[1]).rjust(3)
            c2 = str(c[2]).rjust(3)
            color_text = f"({c0}, {c1}, {c2}, {c[3]})"
            lines.append(f"{name.ljust(max_len)}: {color_text}")

        return "\n".join(lines).strip()

    @error_handler
    def print_style_table(self) -> None:
        print(self._get_style_table())

    def _get_style_table(self) -> str:
        lines: List[str] = []

        col1: List[str] = [
            "",
            "IconStyle",
            "ImageStyle",
            "LineStyle",
            "LineArrowStyle",
            "ShapeStyle",
            "ShapeTextStyle",
            "TextStyle",
        ]

        row_objects = [
            self.iconstyles,
            self.imagestyles,
            self.linestyles,
            self.linearrowstyles,
            self.shapestyles,
            self.shapetextstyles,
            self.textstyles,
        ]

        # create columns
        cols: List[List[str]] = [col1]
        for style_name in self._style_names:
            col: List[str] = [style_name]
            for row_object in row_objects:
                if row_object.has(style_name):
                    col.append("x")
                else:
                    col.append("")
            cols.append(col)

        # modify text length
        cols2 = []
        for col in cols:
            max_length = max(len(s) for s in col)
            padded_strings = [s.ljust(max_length) for s in col]
            cols2.append(padded_strings)

        def draw_border():
            text = "+"
            for col in cols2:
                t = "-" * (len(col[0]) + 2)
                text += f"{t}+"
            lines.append(text)

        for i in range(len(col1)):
            if i == 0:
                draw_border()

            text = "|"
            for col in cols2:
                text += f" {col[i]} |"
            lines.append(text)

            if i == 0:
                draw_border()

            if i == len(col1) - 1:
                draw_border()

        return "\n".join(lines).strip()


def _check_color(color, error_message: str):

    if not isinstance(color, tuple):
        raise ValueError(error_message)
    if len(color) not in [3, 4]:
        raise ValueError(error_message)

    for i in [color[0], color[1], color[2]]:
        if not isinstance(i, int):
            raise ValueError(error_message)
        if not 0 <= i <= 255:
            raise ValueError(error_message)

    if len(color) == 4:
        alpha = color[3]
        if isinstance(alpha, int) or isinstance(alpha, float):
            if 0.0 <= alpha <= 1.0:
                # ok
                ...
            else:
                raise ValueError(error_message)
        else:
            raise ValueError(error_message)


dtheme = Theme()
"""Singleton instance of class ``Theme``."""
