import reflex as rx
import curso_reflex.styles.styles as styles
from curso_reflex.components.link_icon import link_icon
from curso_reflex.styles.styles import Size as Size
from curso_reflex.styles.colors import Color as Color
from curso_reflex.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(title, 
                font_weight="bold", 
                color = Color.PRIMARY.value,),
        body,
        font_size =Size.MEDIUM.value, 
        spacing = "1",
        color = Color.SECONDARY.value,
        )