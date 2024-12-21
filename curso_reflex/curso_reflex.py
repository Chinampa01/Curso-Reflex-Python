import reflex as rx
from rxconfig import config
from curso_reflex.components.navbar import navbar
from curso_reflex.views.header.header import header
from curso_reflex.views.links.links import links
from curso_reflex.components.footer import footer
import curso_reflex.styles.styles as styles
from curso_reflex.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
            ),
        ),
        footer(),
    )

app = rx.App(
    theme=rx.theme(
        accent_color="teal",  # Para representar los detalles neón
        appearance="dark",    # Base oscura como el traje de TD Ekko
        has_background=True,
        ),
    style=styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Rubik+Pixels&display=swap",
    ],
)
app.add_page(index)
app._compile() 