import reflex as rx
from curso_reflex.components.link_button import link_button


def links()->rx.components:
    return rx.vstack(
        link_button()
    )