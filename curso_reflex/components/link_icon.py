import reflex as rx
import curso_reflex.styles.styles as styles

def link_icon(url,tag) -> rx.Component:
    return rx.link(
        rx.icon(
            tag = tag,
            width=styles.Size.BIG.value,
        ),
        href=url,
        is_external=True,
    )