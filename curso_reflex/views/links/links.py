import reflex as rx
from curso_reflex.components.link_button import link_button
from curso_reflex.components.title import title
from curso_reflex.styles.colors import Color as Color
from curso_reflex.styles.colors import TextColor as TextColor
import curso_reflex.styles.styles as styles

def links() -> rx.Component:
    return rx.vstack(
        title("Mis Redes"),
        link_button(
            "instagram",
            "Instagram",
            "Subo memes a diario",
            "#FFFFFF",
            "linear-gradient(300deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #F77737, #FCAF45)",
            {"color":"#FFC107  ","background" : "#FF69B4 ",},
            "https://www.instagram.com/",
        ),
        link_button(
            "facebook",
            "Facebook",
            "Los mismos memes de ig pero en fb",
            "#FFFFFF",
            "#1877F2",
            {"color":"#1877F2", "background" : "#FFC107",},
            "https://www.facebook.com/profile.php?id=100090879346780",
        ),
        link_button(
            "twitter",
            "Threads",
            "Hago comentarios boludos a hilos sin sentido",
            "#FFFFFF",
            "#000000",
            {"color":"#000000","background" : "#FFFFFF",},
            "https://www.threads.net/@cuellar.adriel?xmt=AQGzpw3V2s8zura05__XWIs2tnHp2Vt90MrS6foc_ZcalcA",
        ),
        link_button(
            "gamepad-2",
            "Steam",
            "Juego con los mismos virgochos de siempre",
            "#00ADEE",
            "#171A21",
            {"color":"#171A21","background" : "#00ADEE",},
            "https://steamcommunity.com/id/chin4mpa/",
        ),
        link_button(
            "twitch",
            "Twitch.tv",
            "Hice stream 1 vez y me aburri",
            "#FFFFFF",
            "#9146FF",
            {"color":"#9146FF","background" : "#030303",},
            "https://www.twitch.tv/chinampa01",
        ),
        spacing="4",
        width="100%",
    )