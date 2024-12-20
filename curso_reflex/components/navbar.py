import reflex as rx
import curso_reflex.styles.styles as styles
from curso_reflex.styles.styles import Size as Size

def navbar()->rx.Component:
    return rx.vstack(
        rx.text(
            "Chinampa",
            color = "black",
        ),
        bg = "lightgray",
        position = "sticky",
        padding_x = Size.DEFAULT.value ,
        padding_y = Size.SMALL.value,
        z_index = "999",
        top = "0",
    )