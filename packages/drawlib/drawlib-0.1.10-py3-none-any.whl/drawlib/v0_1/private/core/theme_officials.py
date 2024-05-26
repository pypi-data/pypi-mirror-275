from __future__ import annotations
import dataclasses
from typing import Optional, Dict, Tuple, Union, Literal, List
from copy import deepcopy

from drawlib.v0_1.private.core.model import (
    IconStyle,
    ImageStyle,
    LineStyle,
    LineArrowStyle,
    ShapeStyle,
    ShapeTextStyle,
    TextStyle,
)
from drawlib.v0_1.private.core.fonts import (
    FontBase,
    Font,
    FontSourceCode,
)
from drawlib.v0_1.private.core.colors import Colors

#######################
### Official Themes ###
#######################


def get_default() -> _ThemeReturnValue:
    """Change theme to default.

    Returns:
        None

    """

    # https://coolors.co/6d7cc5-70c2bf-e4dfda-d4b483-c1666b

    # primary color
    blue1 = _get_rgba_from_hex("#12152B")  # line
    blue2 = _get_rgba_from_hex("#6D7CC5")  # fill

    # secondary color
    green1 = _get_rgba_from_hex("#0C1D1C")  # line
    green2 = _get_rgba_from_hex("#70C2BF")  # fill

    # third color
    pink1 = _get_rgba_from_hex("#1D0C0D")  # line
    pink2 = _get_rgba_from_hex("#C1666B")  # fill

    default_template = _ThemeTemplate(
        icon_style="thin",
        icon_color=blue1,
        line_style="solid",
        line_width=2,
        line_color=blue1,
        arrowhead_style="->",
        arrowhead_scale=20,
        shape_line_style="solid",
        shape_line_width=1,
        shape_line_color=blue1,
        shape_fill_color=blue2,
        shapetext_font=Font.SANSSERIF_REGULAR,
        shapetext_size=16,
        shapetext_color=blue1,
        text_font=Font.SANSSERIF_REGULAR,
        text_size=16,
        text_color=blue1,
    )

    blue_template = default_template.copy()

    green_template = default_template.copy()
    green_template.line_color = green1
    green_template.shape_line_color = green1
    green_template.shape_fill_color = green2
    green_template.shapetext_color = green1
    green_template.text_color = green1

    pink_template = default_template.copy()
    pink_template.line_color = pink1
    pink_template.shape_line_color = pink1
    pink_template.shape_fill_color = pink2
    pink_template.shapetext_color = pink1
    pink_template.text_color = pink1

    default_styles = _generate_styles(default_template)
    named_styles = [
        ("blue", list(_generate_styles(blue_template))),
        ("green", list(_generate_styles(green_template))),
        ("pink", list(_generate_styles(pink_template))),
    ]
    named_styles = _add_special_name_styles(default_styles, named_styles)

    theme_colors = [
        ("default", blue2),
        ("blue", blue2),
        ("blue1", blue1),
        ("blue2", blue2),
        ("green", green2),
        ("green1", green1),
        ("green2", green2),
        ("pink", pink2),
        ("pink1", pink1),
        ("pink2", pink2),
    ]

    return _ThemeReturnValue(
        backgroundcolor=(255, 255, 255, 1.0),
        sourcecodefont=FontSourceCode.SOURCECODEPRO,
        iconstyle=default_styles[0],
        imagestyle=default_styles[1],
        linestyle=default_styles[2],
        linearrowstyle=default_styles[3],
        shapestyle=default_styles[4],
        shapetextstyle=default_styles[5],
        textstyle=default_styles[6],
        named_styles=named_styles,
        theme_colors=theme_colors,
    )


def get_flat() -> _ThemeReturnValue:
    # https://flatuicolors.com/palette/defo
    turquoise = (26, 188, 156)
    green_sea = (22, 160, 133)
    emerald = (46, 204, 113)
    nephritis = (39, 174, 96)
    peter_river = (52, 152, 219)
    belize_hole = (41, 128, 185)
    amethyst = (155, 89, 182)
    wisteria = (142, 68, 173)
    wet_asphalt = (52, 73, 94)
    midnight_blue = (44, 62, 80)
    sun_flower = (241, 196, 15)
    orange = (243, 156, 18)
    carrot = (230, 126, 34)
    pumpkin = (211, 84, 0)
    alizarin = (231, 76, 60)
    pomegranate = (192, 57, 43)
    clouds = (236, 240, 241)
    silver = (189, 195, 199)
    concrete = (149, 165, 166)
    asbestos = (127, 140, 141)

    default_color = peter_river
    default_template = _ThemeTemplate(
        icon_style="thin",
        icon_color=midnight_blue,
        line_style="solid",
        line_width=2,
        line_color=midnight_blue,
        arrowhead_style="->",
        arrowhead_scale=20,
        shape_line_style="solid",
        shape_line_width=1,
        shape_line_color=Colors.White,
        shape_fill_color=default_color,
        shapetext_font=Font.SANSSERIF_REGULAR,
        shapetext_size=16,
        shapetext_color=clouds,
        text_font=Font.SANSSERIF_REGULAR,
        text_size=16,
        text_color=midnight_blue,
    )

    """
    turquoise = (26, 188, 156)
    green_sea = (22, 160, 133)
    emerald = (46, 204, 113)
    nephritis = (39, 174, 96)
    peter_river = (52, 152, 219)
    belize_hole = (41, 128, 185)
    amethyst = (155, 89, 182)
    wisteria = (142, 68, 173)
    wet_asphalt = (52, 73, 94)
    midnight_blue = (44, 62, 80)
    sun_flower = (241, 196, 15)
    orange = (243, 156, 18)
    carrot = (230, 126, 34)
    pumpkin = (211, 84, 0)
    alizarin = (231, 76, 60)
    pomegranate = (192, 57, 43)
    clouds = (236, 240, 241)
    silver = (189, 195, 199)
    concrete = (149, 165, 166)
    asbestos = (127, 140, 141)
    """

    named_templates = []
    for name, color in [
        ("turquoise", turquoise),
        ("green_sea", green_sea),
        ("emerald", emerald),
        ("nephritis", nephritis),
        ("peter_river", peter_river),
        ("belize_hole", belize_hole),
        ("amethyst", amethyst),
        ("wisteria", wisteria),
        ("wet_asphalt", wet_asphalt),
        ("midnight_blue", midnight_blue),
        ("sun_flower", sun_flower),
        ("orange", orange),
        ("carrot", carrot),
        ("pumpkin", pumpkin),
        ("alizarin", alizarin),
        ("pomegranate", pomegranate),
        ("clouds", clouds),
        ("silver", silver),
        ("concrete", concrete),
        ("asbestos", asbestos),
    ]:
        t = default_template.copy()
        t.icon_color = color
        t.line_color = color
        if name == "clouds":
            t.shape_fill_color = Colors.White
            t.shape_line_color = midnight_blue
        else:
            t.shape_fill_color = color
        t.text_color = color
        named_templates.append((name, t))

    default_styles = _generate_styles(default_template)
    named_styles = []
    for name, template in named_templates:
        named_styles.append((name, list(_generate_styles(template))))
    named_styles = _add_linearrow_styles(named_styles)

    theme_colors = [
        ("default", peter_river),
    ]

    return _ThemeReturnValue(
        backgroundcolor=(255, 255, 255, 1.0),
        sourcecodefont=FontSourceCode.SOURCECODEPRO,
        iconstyle=default_styles[0],
        imagestyle=default_styles[1],
        linestyle=default_styles[2],
        linearrowstyle=default_styles[3],
        shapestyle=default_styles[4],
        shapetextstyle=default_styles[5],
        textstyle=default_styles[6],
        named_styles=named_styles,
        theme_colors=theme_colors,
    )


def get_gray() -> _ThemeReturnValue:
    """Change theme to gray.

    Returns:
        None

    """

    # https://coolors.co/palette/f8f9fa-e9ecef-dee2e6-ced4da-adb5bd-6c757d-495057-343a40-212529

    # primary color
    gray1 = _get_rgba_from_hex("#212529")  # line color
    gray2 = _get_rgba_from_hex("#ADB5BD")  # fill color

    # secondary color
    gray3 = _get_rgba_from_hex("#CED4DA")

    # third color
    gray4 = _get_rgba_from_hex("#DEE2E6")

    default_template = _ThemeTemplate(
        icon_style="thin",
        icon_color=gray1,
        line_style="solid",
        line_width=2,
        line_color=gray1,
        arrowhead_style="->",
        arrowhead_scale=20,
        shape_line_style="solid",
        shape_line_width=1,
        shape_line_color=gray1,
        shape_fill_color=gray2,
        shapetext_font=Font.SANSSERIF_REGULAR,
        shapetext_size=16,
        shapetext_color=gray1,
        text_font=Font.SANSSERIF_REGULAR,
        text_size=16,
        text_color=gray1,
    )

    gray2_template = default_template.copy()
    gray3_template = default_template.copy()
    gray3_template.shape_fill_color = gray3
    gray4_template = default_template.copy()
    gray4_template.shape_fill_color = gray4

    default_styles = _generate_styles(default_template)
    named_styles = [
        ("gray", list(_generate_styles(gray2_template))),
        ("gray3", list(_generate_styles(gray3_template))),
        ("gray4", list(_generate_styles(gray4_template))),
    ]
    named_styles = _add_special_name_styles(default_styles, named_styles)

    theme_colors = [
        ("gray", gray2),
        ("gray1", gray1),
        ("gray2", gray2),
        ("gray3", gray3),
        ("gray4", gray4),
    ]

    return _ThemeReturnValue(
        backgroundcolor=(255, 255, 255, 1.0),
        sourcecodefont=FontSourceCode.SOURCECODEPRO,
        iconstyle=default_styles[0],
        imagestyle=default_styles[1],
        linestyle=default_styles[2],
        linearrowstyle=default_styles[3],
        shapestyle=default_styles[4],
        shapetextstyle=default_styles[5],
        textstyle=default_styles[6],
        named_styles=named_styles,
        theme_colors=theme_colors,
    )


############
### Data ###
############


@dataclasses.dataclass
class _ThemeTemplate:
    """Helper dataclass for defining theme styles"""

    def copy(self) -> _ThemeTemplate:
        return deepcopy(self)

    # icon
    icon_style: Literal["thin", "light", "regular", "bold", "fill"]
    icon_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]

    # line
    line_style: Literal["solid", "dashed", "dotted", "dashdot"]
    line_width: float
    line_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]
    arrowhead_style: Literal[
        "->",
        "<-",
        "<->",
        "-|>",
        "<|-",
        "<|-|>",
    ]
    arrowhead_scale: int

    # shape
    shape_line_style: Literal["solid", "dashed", "dotted", "dashdot"]
    shape_line_width: float
    shape_line_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]
    shape_fill_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]

    # shapetext
    shapetext_font: FontBase
    shapetext_size: int
    shapetext_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]

    # text
    text_font: FontBase
    text_size: int
    text_color: Union[
        Tuple[float, float, float],
        Tuple[float, float, float, float],
    ]


@dataclasses.dataclass
class _ThemeReturnValue:
    backgroundcolor: Tuple[int, int, int, float]
    sourcecodefont: FontSourceCode
    iconstyle: IconStyle
    imagestyle: ImageStyle
    linestyle: LineStyle
    linearrowstyle: LineArrowStyle
    shapestyle: ShapeStyle
    shapetextstyle: ShapeTextStyle
    textstyle: TextStyle

    named_styles: List[
        Tuple[
            str,
            List[
                Union[
                    IconStyle,
                    ImageStyle,
                    LineStyle,
                    LineArrowStyle,
                    ShapeStyle,
                    ShapeTextStyle,
                    TextStyle,
                ]
            ],
        ]
    ]

    theme_colors: List[
        Tuple[
            str,
            Union[
                Tuple[int, int, int],
                Tuple[int, int, int, float],
            ],
        ],
    ]


############
### Util ###
############


def _get_rgba_from_hex(hex_color: str) -> Tuple[int, int, int, float]:
    """
    Convert a hexadecimal color code to RGBA values.

    Args:
        hex_color (str): The hexadecimal color code (e.g., "#FF5733" or "#FFF").

    Returns:
        tuple[int, int, int, float]: A tuple containing the RGBA values (0-255 for R, G, B and 0.0-1.0 for A).
    """

    # Remove the '#' prefix if present
    hex_color = hex_color.lstrip("#")

    # Determine the length of the hex color code
    hex_length = len(hex_color)

    # Convert the hex code to RGB values
    if hex_length == 3:  # Short hex format (#RGB)
        r = int(hex_color[0] * 2, 16)
        g = int(hex_color[1] * 2, 16)
        b = int(hex_color[2] * 2, 16)
        a = 1.0
    elif hex_length in (6, 8):  # Full hex format (#RRGGBB)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        if hex_length == 8:  # With alpha
            a = int(hex_color[6:8], 16)
        else:
            a = 1.0
    else:
        raise ValueError("Invalid hex color code format")

    return (r, g, b, a)


def _generate_styles(
    template: _ThemeTemplate,
) -> Tuple[IconStyle, ImageStyle, LineStyle, LineArrowStyle, ShapeStyle, ShapeTextStyle, TextStyle]:

    icon = IconStyle(
        style=template.icon_style,
        color=template.icon_color,
        halign="center",
        valign="center",
    )
    image = ImageStyle(
        lwidth=0,
        lstyle=template.shape_line_style,
        lcolor=template.shape_line_color,
        halign="center",
        valign="center",
    )
    line = LineStyle(
        style=template.line_style,
        width=template.line_width,
        color=template.line_color,
    )
    linearrow = LineArrowStyle(
        lstyle=template.line_style,
        lwidth=template.line_width,
        hstyle=template.arrowhead_style,
        hscale=template.arrowhead_scale,
        color=template.line_color,
    )
    shape = ShapeStyle(
        lwidth=template.shape_line_width,
        lstyle=template.shape_line_style,
        lcolor=template.shape_line_color,
        fcolor=template.shape_fill_color,
        halign="center",
        valign="center",
    )
    shapetext = ShapeTextStyle(
        font=template.text_font,
        size=template.text_size,
        color=template.text_color,
        halign="center",
        valign="center",
    )
    text = TextStyle(
        font=template.text_font,
        size=template.text_size,
        color=template.text_color,
        halign="center",
        valign="center",
    )

    return (icon, image, line, linearrow, shape, shapetext, text)


def _add_special_name_styles(
    default_styles: Union[
        IconStyle,
        ImageStyle,
        LineStyle,
        LineArrowStyle,
        ShapeStyle,
        ShapeTextStyle,
        TextStyle,
    ],
    named_styles: List[
        Tuple[
            str,
            List[
                Union[
                    IconStyle,
                    ImageStyle,
                    LineStyle,
                    LineArrowStyle,
                    ShapeStyle,
                    ShapeTextStyle,
                    TextStyle,
                ]
            ],
        ]
    ],
) -> List[
    Tuple[
        str,
        List[
            Union[
                IconStyle,
                ImageStyle,
                LineStyle,
                LineArrowStyle,
                ShapeStyle,
                ShapeTextStyle,
                TextStyle,
            ]
        ],
    ]
]:
    new_named_styles = deepcopy(named_styles)

    # add white ShapeTextStyle
    has_named_style_white = False
    for named_style in new_named_styles:
        name = named_style[0]
        if name == "white":
            has_named_style_white = True

    if not has_named_style_white:
        default_shapetextstyle = default_styles[5]
        if not isinstance(default_shapetextstyle, ShapeTextStyle):
            raise ValueError()
        white_shapetextstyle = default_shapetextstyle.copy()
        white_shapetextstyle.color = Colors.White
        new_named_styles.append(("white", [white_shapetextstyle]))

    # add IconStyle and LineArrowStyle with new names
    inserted = 0
    for i, (name, styles) in enumerate(named_styles, start=1):
        icon, image, line, linearrow, shape, shapetext, text = styles

        lc_list = []
        fc_list = []
        la_list = []
        lafc_list = []

        if isinstance(icon, IconStyle) and isinstance(shape, ShapeStyle):
            icon_lcolor = icon.copy()
            icon_lcolor.color = shape.lcolor
            icon_fcolor = icon.copy()
            icon_fcolor.color = shape.fcolor
            lc_list.append(icon_lcolor)
            fc_list.append(icon_fcolor)
        else:
            raise ValueError()

        if isinstance(line, LineStyle):
            line_fcolor = line.copy()
            line_fcolor.color = shape.fcolor
            fc_list.append(line_fcolor)
        else:
            raise ValueError()

        if isinstance(linearrow, LineArrowStyle):
            linearrow_fcolor = linearrow.copy()
            linearrow_fcolor.color = shape.fcolor
            la_list.append(linearrow)
            lafc_list.append(linearrow_fcolor)
        else:
            raise ValueError()

        if len(lc_list) != 0:
            new_named_styles.insert(i + inserted, (f"lc-{name}", lc_list))
            inserted += 1
        if len(fc_list) != 0:
            new_named_styles.insert(i + inserted, (f"fc-{name}", fc_list))
            inserted += 1
        if len(la_list) != 0:
            new_named_styles.insert(i + inserted, (f"la-{name}", la_list))
            inserted += 1
        if len(lafc_list) != 0:
            new_named_styles.insert(i + inserted, (f"lafc-{name}", lafc_list))
            inserted += 1

    return new_named_styles


def _add_linearrow_styles(
    named_styles: List[
        Tuple[
            str,
            List[
                Union[
                    IconStyle,
                    ImageStyle,
                    LineStyle,
                    LineArrowStyle,
                    ShapeStyle,
                    ShapeTextStyle,
                    TextStyle,
                ]
            ],
        ]
    ],
) -> List[
    Tuple[
        str,
        List[
            Union[
                IconStyle,
                ImageStyle,
                LineStyle,
                LineArrowStyle,
                ShapeStyle,
                ShapeTextStyle,
                TextStyle,
            ]
        ],
    ]
]:
    new_named_styles = deepcopy(named_styles)
    inserted = 0
    for i, (name, styles) in enumerate(named_styles, start=1):
        icon, image, line, linearrow, shape, shapetext, text = styles

        if isinstance(linearrow, LineArrowStyle):
            new_named_styles.insert(i + inserted, (f"la-{name}", [linearrow]))
            inserted += 1
        else:
            raise ValueError()

    return new_named_styles
