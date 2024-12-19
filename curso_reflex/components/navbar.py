import reflex as rx
def navbar()->rx.Component:
    return rx.vstack(
        rx.text(
            "Chinampa",
            font_family = "arial",
            height = "40px",
            direction = "column",
            width = "100%",
        ),
        bg = "blue",
        position = "sticky",
        padding_x = "16px" ,
        padding_y = "8px",
        z_index = "999",
        border= "1px solid",
        align="center",
        spacing="4",
        width = "100%",
    )