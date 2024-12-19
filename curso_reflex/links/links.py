
import reflex as rx
from curso_reflex.components.link_button import link_button
from curso_reflex.components.title import title

def links()->rx.components:
    return rx.vstack(
        title("Mis Links"),
        link_button(
            "GitHub",
            "https://github.com/Chinampa01",
            width = "100%",
            ),
        link_button(
            "LinkedIn"
            ,"https://www.linkedin.com/in/adriel-josu%C3%A9-cuellar-a%C3%B1azco-488028247/",
            width = "100%",
            ),
        align="center",
        spacing="4",
        width = "100%",
    ) 