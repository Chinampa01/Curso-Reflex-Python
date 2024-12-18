import reflex as rx

def navbar()->rx.Component:
    return rx.hstack(
        rx.text(
            "Chinampa",
            font_family = "arial",
            height = "40px",
        ),
        bg = "blue",
        position = "sticky",
        padding_x = "16px" ,
        padding_y = "8px",
        z_index = "999",
        width = "100px",
        border= "1px solid",
    )