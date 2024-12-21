import reflex as rx
import curso_reflex.styles.styles as styles
from curso_reflex.styles.styles import Size as Size
from curso_reflex.styles.colors import Color as Color
from curso_reflex.styles.colors import TextColor as TextColor
import curso_reflex.styles.styles as styles


def navbar()->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Chi",color= Color.PRIMARY.value),
            rx.text("nam",color = Color.SECONDARY.value),
            rx.text("pa",color = Color.TERCIARY.value),
            spacing = "0",
            style = styles.navbar_title_style,
        ),   
        position = "sticky",
        padding_x = Size.BIG.value ,
        padding_y = Size.DEFAULT.value,
        z_index = "999",
        top = "0",
    )