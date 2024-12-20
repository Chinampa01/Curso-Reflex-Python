import reflex as rx
import curso_reflex.styles.styles as styles

def link_button(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_big_right",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),  
                ),
            ),
        ),
        href=url,
        is_external=True,
    )  

    
   