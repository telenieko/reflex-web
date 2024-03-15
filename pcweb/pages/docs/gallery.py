import pandas as pd

import reflex as rx
from pcweb import constants, styles
from pcweb.styles import text_colors as tc
from pcweb.templates.webpage import webpage

# every app must have at least one tag in order to be rendered
apps_list = [
    {
        "name": "Reflex",
        "difficulty": "Advanced",
        "tags": ["Multi-Page", "Graphs",  "Data App", "Database"],
        "description": "This website!",
        "img": "/gallery/pcweb.png",
        "gif": "",
        "url": "https://pynecone.io/",
        "source": "https://github.com/pynecone-io/pcweb",
    },
    {
        "name": "Chat App",
        "difficulty": "Advanced",
        "tags": ["Multi-Page", "AI", "Custom Components"],
        "description": "An AI chat app.",
        "img": "/gallery/chat.gif",
        "gif": "",
        "url": "https://webui-teal-star.reflex.run",
        "source": "https://github.com/reflex-dev/reflex-chat",
    },
    {
        "name": "Email Gen",
        "difficulty": "Intermediate",
        "tags": ["AI", "Database"],
        "description": "A sales email generator using OpenAI's GPT3 API.",
        "img": "/gallery/sales.png",
        "gif": "",
        "url": "https://sales.reflex.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
    },
    {
        "name": "DALL-E",
        "difficulty": "Beginner",
        "tags": ["AI"],
        "description": "An app to generate images using OpenAI's DALL-E model.",
        "img": "/gallery/dalle.png",
        "gif": "/gallery/dalle.gif",
        "url": "https://dalle.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/dalle",
    },
    {
        "name": "Graphing Traversal",
        "difficulty": "Intermediate",
        "tags": ["Graphs"],
        "description": "A graphing traversal app.",
        "img": "/gallery/traversal.png",
        "gif": "",
        "url": "https://traversal.reflex.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/traversal",
    },
    {
        "name": "GPT Q&A",
        "difficulty": "Advanced",
        "tags": ["AI", "Auth", "Database"],
        "description": "An UI around Open AI's GPT3 API.",
        "img": "/gallery/gpt.png",
        "gif": "/gallery/gpt.gif",
        "url": "",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/gpt",
    },
    {
        "name": "NBA",
        "difficulty": "Intermediate",
        "tags": ["Graphs", "Database", "Data App"],
        "description": "An interactive dashboard for NBA data.",
        "img": "/gallery/nba.png",
        "gif": "/gallery/nba.gif",
        "url": "https://nba.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/nba",
    },
    {
        "name": "Quiz",
        "difficulty": "Intermediate",
        "tags": [ "Data App", "Database"],
        "description": "A quiz app that will test your Python knowledge.",
        "img": "/gallery/quiz.png",
        "gif": "/gallery/quiz.gif",
        "url": "https://quiz.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/quiz",
    },
    {
        "name": "Twitter Clone",
        "difficulty": "Beginner",
        "tags": ["Auth", "Database", "Multi-Page"],
        "description": "A twitter clone with a login system and database.",
        "img": "/gallery/twitter.png",
        "gif": "/gallery/twitter.gif",
        "url": "",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/twitter",
    },
    {
        "name": "Translator",
        "difficulty": "Beginner",
        "tags": [],
        "description": "A translator app.",
        "img": "/gallery/translator.png",
        "gif": "/gallery/translator.gif",
        "url": "https://translator.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/translator",
    },
    {
        "name": "Clock",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "An analog clock with different time zones.",
        "img": "/gallery/clock.png",
        "gif": "/gallery/clock.gif",
        "url": "https://clock.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/clock",
    },
    {
        "name": "Background Tasks",
        "difficulty": "Intermediate",
        "tags": ["Streaming"],
        "description": "An app that showcases simple Background tasks.",
        "img": "/gallery/simple_background_tasks.png",
        "gif": "/gallery/simple_background_tasks.gif",
        "url": "https://simple-background-tasks.reflex.run",
        "source": "https://github.com/reflex-dev/reflex-examples/tree/main/lorem-stream",
    },
]

community_apps_list = [
    {
        "name": "Half Truth",
        "difficulty": "Intermediate",
        "tags": ["AI"],
        "description": "A game where half the statements are facts and half are fibbs.",
        "img": "/gallery/half_truth.png",
        "gif": "",
        "url": "https://halftruth.reflex.run",
        "source": "https://github.com/romankouz/hacktoberfest/tree/5050_official/submissions/miscellaneous/romankouz_half_truth",
    },
    {
        "name": "Git Gold Book",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "An overview about about pull requests for a particular repo.",
        "img": "/gallery/git_gold_book.png",
        "gif": "",
        "url": "https://git-app-gold-book.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/data_visualizations/ashish_git_App",
    },
    {
        "name": "Dataframe Chatbot",
        "difficulty": "Intermediate",
        "tags": ["AI"],
        "description": "Users can interact with their dataframe using natural language.",
        "img": "/gallery/dataframechatbot.png",
        "gif": "",
        "url": "https://interactwithyourcsv.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/interactive_db/emmanuel/my_dataframe_chatbot",
    },
    {
        "name": "Text Summarizer",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "An app to summarize text.",
        "img": "/gallery/text_summarizer.png",
        "gif": "",
        "url": "https://textsummarizer.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/ai_apps/emmanuel/text_summarizer",
    },
    {
        "name": "Reflex Rave",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "A movie recommendation system.",
        "img": "/gallery/reflexrave.png",
        "gif": "",
        "url": "https://reflexrave.reflex.run",
        "source": "https://github.com/HeetVekariya/hacktoberfest/tree/heet/ReflexRave",
    },
    {
        "name": "Fynesse",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "Spotify recommendations generator with control.",
        "img": "/gallery/fynesse.png",
        "gif": "",
        "url": "https://fynesse.reflex.run",
        "source": "https://github.com/wightwick/fynesse",
    },
    {
        "name": "User Landing Page",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "Site for representing user links of interest and social networks.",
        "img": "/gallery/mouredev.jpg",
        "gif": "",
        "url": "https://moure.dev",
        "source": "https://github.com/mouredev/python-web",
    },
]

apps_df = pd.DataFrame(apps_list)


def create_list_of_tags(dataframe: pd.DataFrame) -> list:
    """This function takes our pandas dataframe and returns all types of tags
    that exist across all our apps
    .
    """
    # Extract the "tags" column from the DataFrame
    tags_column = dataframe["tags"]

    # Convert the "tags" column to a list
    tags_list = tags_column.tolist()

    # Flatten the list of lists into a single list
    flattened_tags = [tag for sublist in tags_list for tag in sublist]

    # Create a set of unique tags
    unique_tags_set = set(flattened_tags)

    # Convert the set back to a list if needed
    unique_tags_list = list(unique_tags_set)
    return unique_tags_list


list_of_tags = create_list_of_tags(apps_df)


class SideBarState(rx.State):
    """Side Bar State."""

    community_apps_list: list[dict[str, str]] = community_apps_list

    chosen_tags_dict: dict[str, bool] = {key: False for key in list_of_tags}

    def update_tag(self, name: str):
        self.chosen_tags_dict[name] = not self.chosen_tags_dict[name]

    @rx.cached_var
    def true_tags(self) -> list:
        """This function returns a list of the tags selected in the UI, if no tags
        are selected then it returns all the tags
        .
        """
        true_keys = [key for key, value in self.chosen_tags_dict.items() if value]
        if not true_keys:
            return list(self.chosen_tags_dict)
        return list(true_keys)

    @rx.cached_var
    def data_to_return(self) -> list[dict[str, str]]:
        """This function iterates over all the apps we have and if the app has one of the
        tags we have selected in true_tags then it will render this app in the UI
        .
        """
        selected_examples = []
        for example_dict in apps_list:
            example_tags = set(example_dict["tags"])
            if example_tags.intersection(self.true_tags):
                selected_examples.append(example_dict)
        return selected_examples


border_radius = ("0.375rem",)
box_shadow = ("0px 0px 0px 1px rgba(84, 82, 95, 0.14)",)
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"

def add_item(category):
    return rx.flex(
        rx.box(
            height="12rem",
            width="100%",
            background_image='url('+category["img"]+')',
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            border_radius= "8px 8px 0 0"
        ),
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        category["name"],
                        size="4",
                        color="#D6D6ED"
                    ),
                    rx.box(
                        flex_grow=1,
                    ),
                    rx.box(
                        category["difficulty"], 
                        border= "1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);",
                        color="#6C6C81",
                        padding_x=".25em",
                        font_size="0.75em",
                        border_radius="6px",
                    ),
                    width="100%",
                    justify_content="center"
                ),
                rx.text(category["description"], size="1", color="#8E8EA8"),
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
            rx.text("Author: Reflex", color="#8E8EA8", font_size="0.75em"),
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
        height="19em"
    )

grid_layout=[1, 2, 2, 3, 3, 4]

def component_grid():
    return rx.chakra.responsive_grid(
            rx.foreach(SideBarState.data_to_return, add_item),
            columns=grid_layout,
            gap=6,
        )

def community_component_grid():
    return rx.chakra.responsive_grid(
            rx.foreach(SideBarState.community_apps_list, add_item),
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
                is_active=SideBarState.chosen_tags_dict[tag],
                on_click=SideBarState.update_tag(tag),
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

def gallery_heading():
    return rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Apps made in Reflex", 
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
                "Reflex Gallery", 
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing= "-1.28px;",
            ),
            rx.text(
                "Here are some examples of what the team and community has made with Reflex. ",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            padding_bottom="1em",
        )

def community_heading():
    return rx.vstack(
            rx.chakra.text(
                "Community Gallery", 
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing= "-1.28px;",
            ),
            rx.text(
                "Here are some examples of what the team and community has made with Reflex. ",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            padding_y="2em",
        )

@webpage(path="/docs/gallery", title="Gallery · Reflex")
def gallery() -> rx.Component:
    return rx.chakra.vstack(
        gallery_heading(),
        rx.vstack(
            sidebar_component_grid(list_of_tags),
            component_grid(),
            community_heading(),
            community_component_grid(),
            align_items="left",
            padding_x="1em",
            padding_y="8em",
        ),
        max_width="80em",
        margin_x="auto",
        margin_top="40px",
        height="100%",
    )
