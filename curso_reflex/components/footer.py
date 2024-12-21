import reflex as rx
import datetime
from curso_reflex.styles.styles import Size as Size
from curso_reflex.styles.colors import Color as Color
from curso_reflex.styles.colors import TextColor as TextColor

def footer() ->rx.components:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"© 2023 - {datetime.date.today().year} Chinampa by Adriel Cuellar. Python Developer", 
                font_size=Size.MEDIUM.value, color = TextColor.FOOTER.value,margint_top = Size.ZERO.value),
        margin_bottom = Size.BIG.value,
        paddin_bottom = Size.BIG.value,
        color = TextColor.FOOTER.value,
        width="100%",
        align="center",
        spacing="4",
    )