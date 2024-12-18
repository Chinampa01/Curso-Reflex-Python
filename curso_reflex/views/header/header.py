import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AC", variant="soft",size = "3"),
        rx.text("@Chinampa"),
        rx.text(f"""Hola 👋 Mi nombre es Adriel Cuellar
                Actualmente estoy en proceso de aprendizaje constante
                principalmente en tecnologías relacionadas
                con python manejando herramientas tanto de backend
                y frontend
                Aquí podrás encontrar mi material trabajado y 
                conocimiento adquirido junto con enlances de interes.
                ¡BIENVENID@!"""),
        
        
    )