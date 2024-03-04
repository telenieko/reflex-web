import reflex as rx
from pcweb import styles
from pcweb.styles import font_weights as fw

heading_style2 = {
    "background_color": rx.color_mode_cond(rx.color('violet', 3), rx.color('violet', 2)),
    "border_radius": "0.5em",
    "width": "100%",
    "padding_left": "0.5em",
    "padding_right": "0.5em",
}
heading_style3 = {
    "font_weight": fw["section"],
    "font_size": styles.TEXT_FONT_SIZE,
    "color": "#696287",
    "margin_bottom": "0.5em",
    "margin_left": "1.1em",
}
