"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from curso_reflex.components.navbar import navbar
from curso_reflex.views.header.header import header
from curso_reflex.views.links.links import links
from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
        navbar(),
        header(),
        links(),
        ),
        direction = "column"
    )


app = rx.App()
app.add_page(index)
app._compile()
