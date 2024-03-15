import reflex as rx
from pcweb.templates.webpage import webpage
import httpx
import datetime

# every app must have at least one tag in order to be rendered
components_list = [
    {
        "package_name": "reflex-motion",
        "tags": [],
        "description": "A motion library for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-chat",
        "tags": [],
        "description": "A chat component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-local-auth",
        "tags": [],
        "description": "Local authentication for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-image-zoom",
        "tags": [],
        "description": "A zoomable image component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-webcam",
        "tags": [],
        "description": "A webcam component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-spline",
        "tags": [],
        "description": "A wrapper for the Spline design tool.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-color-picker",
        "tags": [],
        "description": "A color picker component for Reflex.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },
    {
        "package_name": "reflex-simpleicons",
        "tags": [],
        "description": "SVG icons from the most popular brands.",
        "img": "https://reflexjs.org/static/preview.png",
        "github": ""
    },

]

def fetch_url(url):
    """Helper function to fetch data from a given URL."""
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {url}: {response.status_code} - {response.text}")
            return None
        
def get_downloads(package_name):
    """Fetch the total downloads for the last month for a given package."""
    today = datetime.date.today()
    first_day_of_current_month = datetime.date(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_current_month - datetime.timedelta(days=1)
    first_day_of_last_month = datetime.date(last_day_of_last_month.year, last_day_of_last_month.month, 1)

    start_date = first_day_of_last_month.strftime('%Y-%m-%d')
    end_date = last_day_of_last_month.strftime('%Y-%m-%d')

    url = f"https://pypistats.org/api/packages/{package_name}/recent?start_date={start_date}&end_date={end_date}"
    data = fetch_url(url)

    if data:
        return data.get('data', {}).get('last_month', 0)
    return 0

def get_package_info(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch package info: {response.status_code} - {response.text}")
            return {}


def add_item(category):

    package_info = get_package_info(category["package_name"])

    return rx.flex(
        # rx.box(
        #     height="12rem",
        #     width="100%",
        #     background_image='url('+category["img"]+')',
        #     background_size="cover",
        #     background_position="center",
        #     background_repeat="no-repeat",
        #     border_radius= "8px 8px 0 0"
        # ),
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        category["package_name"],
                        size="4",
                        color="#D6D6ED"
                    ),
                    rx.box(
                        flex_grow=1,
                    ),
                    rx.hstack(
                        str(get_downloads(category["package_name"])), 
                        rx.icon(
                            tag="download",
                            size=12
                        ),
                        border= "1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);",
                        color="#6C6C81",
                        padding_x=".25em",
                        font_size="0.75em",
                        border_radius="6px",
                        justify="center",
                    ),
                    width="100%",
                    justify_content="center"
                ),
                rx.text(
                    category["description"],
                    size="1", 
                    color="#8E8EA8"
                ),
                align_items="start",
                width="100%",
            ),
            width="100%",
            height="5em",
            padding_top="1em",
            align_items="start",
            padding_x=".75em",
        ),
        rx.box(
            flex_grow=1,
        ),
        rx.hstack(
            rx.text(
                "Author: " + package_info.get("info", {}).get("author", "Unknown"),
                color="#8E8EA8", 
                font_size="0.75em"
            ),
            rx.spacer(),
            rx.icon(
                tag="external-link",
                color="rgba(186, 199, 247, 0.12)",
                size=16
            ),
            width = "100%",
            justify="center",
            padding_x=".75em",
            padding_bottom=".25em",
        ),
        direction="column",
        border= "1px solid #3C3646;",
        border_radius="8px",
        height="7em"
    )

grid_layout=[1, 2, 2, 3, 3, 4]

def component_grid():
    return rx.chakra.responsive_grid(
            *[
                add_item(category)
                for category in components_list
            ],
            columns=grid_layout,
            gap=6,
        )

def sidebar_component_grid(tags):
    return rx.chakra.wrap(
        *[
            rx.chakra.button(
                tag,
                border_radius="15px",
                padding_x=".5em",
                is_active=CustomComponentState.chosen_tags_dict[tag],
                on_click=CustomComponentState.update_tag(tag),
                color="#6C6C81",
                background="rgba(161, 157, 213, 0.05);",
                _hover={
                    "border": "1px solid rgba(102, 90, 241, 0.80);"
                },
                _active={
                    "border": "1px solid rgba(102, 90, 241, 0.80);",
                    "background": "rgba(102, 90, 241, 0.15);",

                },
                _checked={
                    "border": "rgba(186, 199, 247, 0.12)",
                    "bg": "#5B4BF0",
                },
            )
            for tag in tags
        ],
        padding_bottom="2em",
        align_items="left",
        width="100%",
    )

def heading():
    return rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Component Gallery", 
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em"
                ),
                border_radius= "15px;",
                border= "1px solid #4435D4;",
                background= "linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow= "0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Custom Components", 
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing= "-1.28px;",
            ),
            rx.text(
                "Here are some examples of what the team and community has made with Reflex.",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            padding_bottom="1em",
        )

@webpage(path="/docs/custom-components", title="Custom Components · Reflex")
def custom_components() -> rx.Component:
    return rx.chakra.vstack(
        heading(),
        rx.vstack(
            component_grid(),
            align_items="left",
            padding_x="1em",
            padding_y="8em",
        ),
        max_width="80em",
        margin_x="auto",
        margin_top="40px",
        height="100%",
    )
