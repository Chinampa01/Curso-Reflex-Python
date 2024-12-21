import reflex as rx
import curso_reflex.styles.styles as styles
from curso_reflex.styles.colors import Color as Color

def link_button(tag: str, text_title:str, text_body:str, color : str, background : str,hover: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=tag,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    
                    
                ),
                rx.vstack(
                    rx.text(text_title, style=styles.button_title_style,),
                    rx.text(text_body, style=styles.button_body_style),
                ),
                spacing = "3",
            ),
            color = color,
            background = background,
            _hover = hover,
        ),
        href=url,
        is_external=True,
    )  

    
   