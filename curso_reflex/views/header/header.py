import reflex as rx
import curso_reflex.styles.styles as styles
from curso_reflex.components.link_icon import link_icon
from curso_reflex.components.info_text import info_text
from curso_reflex.styles.styles import Size as Size
from curso_reflex.styles.colors import Color as Color
from curso_reflex.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar("""src="/Michi_Ekko.jpg""", fallback="AC", size="8"),
            rx.vstack(
                rx.heading("Adriel Cuellar",size = "8", color = TextColor.HEADER.value),
                rx.text("Estudiante de Licenciatura en Sistemas",size = "3",margin_top = "0px !important", color = TextColor.FOOTER.value),
                rx.hstack(
                    link_icon("https://www.linkedin.com/in/adriel-josu%C3%A9-cuellar-a%C3%B1azco-488028247/",
                                tag = "linkedin"),
                    link_icon("https://github.com/Chinampa01",
                                tag = "github"),
                    link_icon("https://drive.google.com/open?id=1-3zbhzYWUBSucxWCuhSnvpp8djwpFSk_&usp=drive_fs",
                                tag = "file-text"),
                    spacing = "3",
                    ),
                spacing = "4",
                ),
        ),
        rx.flex(
            info_text("Sobre ", "mi:"),
        ),
        
        
        rx.text("""Actualmente estoy en proceso de aprendizaje constante,
                    principalmente en tecnologías relacionadas
                    con python manejando herramientas tanto de backend
                    y frontend.""",
                    color = TextColor.BODY.value),
        rx.text("""Aquí podrás encontrar mi material trabajado y 
                conocimiento adquirido junto con enlances de interes.
                ¡BIENVENID@!""",
                color = TextColor.BODY.value),
       spacing = "6",
    ),
   