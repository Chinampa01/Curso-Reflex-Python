import reflex as rx
import datetime
def footer() ->rx.components:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"© 2023 - {datetime.date.today().year} Chinampa by Adriel Cuellar. Python Developer"),
        width="100%",
        align="center",
        spacing="4"
    )