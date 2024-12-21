import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
# Constants
MAX_WIDTH = "35em"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background_color": Color.PRIMARY.value,
        "color": Color.SECONDARY.value,
        "font_weight": "bold", 
        "_hover":{
            "background_color": Color.SECONDARY.value,
            "color": Color.PRIMARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
        "width": "100%",
    },
}

navbar_title_style = dict(
    font_family = "Rubik Pixels",
    font_size = Size.LARGE.value,
)


title_style = dict(
    width="bold",
    padding_top=Size.DEFAULT.value,
    color = TextColor.HEADER.value,
)
button_title_style = dict(
    font_size=Size.LARGE.value
)
button_body_style = dict(
    font_size=Size.MEDIUM.value
)