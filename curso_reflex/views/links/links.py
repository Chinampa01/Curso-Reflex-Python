import reflex as rx
from curso_reflex.components.link_button import link_button


def links()->rx.components:
    return rx.vstack(
        link_button("GitHub","https://github.com/Chinampa01"),
        link_button("LinkedIn","https://www.linkedin.com/in/adriel-josu%C3%A9-cuellar-a%C3%B1azco-488028247/"),
        
    )