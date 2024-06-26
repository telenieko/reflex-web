"""UI and logic for the navbar component."""
import reflex as rx
from .buttons.github import github
from .buttons.discord import discord
from .buttons.sidebar import sidebar_button
from .search import search_bar

from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.faq import faq
from pcweb.pages.docs.library import library
from pcweb.pages.blog import blg
from pcweb.pages.changelog import changelog
from pcweb.pages.docs.gallery import gallery


def resource_header(text):
    return rx.text(
        text, color=rx.color_mode_cond(rx.color("mauve", 12), rx.color("mauve", 10)), padding_bottom="10px", font_weight="600"
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 9)),
            rx.text(text, color=rx.color("mauve", 9)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )


def resources_section(style):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.flex(
                rx.text("Resources", style=style),
                rx.icon(tag="chevron_down", size=18, style=style),
                align_items="center",
                _hover={
                    "cursor": "pointer",
                },
                spacing="2",
            )
        ),
        rx.hover_card.content(
            rx.flex(
                rx.flex(
                    resource_header("Open Source"),
                    resources_item("Github", "https://github.com/reflex-dev", "github"),
                    resources_item(
                        "Github Discussions",
                        "https://github.com/orgs/reflex-dev/discussions",
                        "message-circle-question",
                    ),
                    resources_item(
                        "Contribute to Reflex",
                        "https://github.com/reflex-dev/reflex/blob/main/CONTRIBUTING.md",
                        "file-json-2",
                    ),
                    resources_item("Changelog", changelog.path, "list-checks"),
                    direction="column",
                    align_items="start",
                    padding_left="20px",
                    padding_y="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Resources"),
                    resources_item(
                        "Component Library", library.path, "layout-panel-left"
                    ),
                    resources_item(
                        "Roadmap",
                        "https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37",
                        "map-pinned",
                    ),
                    resources_item("Blog", blg.path, "text"),
                    resources_item("FAQ", faq.path, "list-todo"),
                    direction="column",
                    align_items="start",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Hosting"),
                    resources_item(
                        "Deployment", hosting.deploy_quick_start.path, "globe"
                    ),
                    resources_item(
                        "Self-Hosting", hosting.self_hosting.path, "server"
                    ),
                    direction="column",
                    background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
                    border_left="1px solid rgba(29, 29, 32, 0.08);",
                    align_items="start",
                    height="210px",
                    padding_top="20px",
                    padding_left="20px",
                    padding_bottom="20px",
                    padding_right="20px",
                    spacing="2",
                ),
                spacing="6",
            ),
            border="1px solid rgba(29, 29, 32, 0.08);",
            background="linear-gradient(180deg, rgba(29, 27, 33, 0.95) 0%, rgba(20, 19, 24, 0.95) 100%);",
            box_shadow="0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;",
            max_width="1000px",
            height="210px",
            padding="0",
            overflow="hidden",
        ),
    )


def navigation_section():

    section_style={
        "color": "#6C6C81",
        "font-weight": "400",
    }

    return rx.box(
        rx.flex(
            rx.link("Docs", href=getting_started.introduction.path, style=section_style),
            rx.link("Blog", href=blg.path, style=section_style),
            rx.link("Gallery", href=gallery.path, style=section_style),
            resources_section(style=section_style),
            spacing="5",
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
    )

def blur_background():
    return rx.fragment(
        rx.script(
            """
            window.onscroll = function() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                var scrollThreshold = 100;
                var navbar = document.getElementById('navbar');

                if (scrollTop > scrollThreshold) {
                    navbar.classList.add('blur-navbar');
                } else {
                    navbar.classList.remove('blur-navbar');
                }
            };
            """
        ),
        rx.html(
            """
            <style>
            .blur-navbar {
                border: 1px solid rgba(29, 29, 32, 0.08);
                background: linear-gradient(180deg, rgba(29, 27, 33, 0.98) 0%, rgba(20, 19, 24, 0.98) 100%);
                box-shadow: 0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;
                backdrop-filter: blur(20px);
            }
            </style>
            """
        )
    )

def navbar(sidebar: rx.Component = None) -> rx.Component:
    return rx.flex(
        rx.link(
            rx.box(
                rx.image(
                        src="/logos/dark/reflex.svg",
                        alt="Reflex Logo",
                        height="20px",
                        justify="start",
                    ),
            ),
            href="/",
        ),
        navigation_section(), 
        rx.box(
            flex_grow="1",
        ),
        rx.flex(
            search_bar(),
            github(),
            rx.divider(size="2", color=rx.color("mauve"), orientation="vertical"),
            rx.box(
                discord(),
                display=["none", "none", "none", "none", "flex", "flex"],
            ),
            rx.box(
                sidebar_button(sidebar),
                display=["flex", "flex", "flex", "flex", "none", "none"],
            ),
            spacing="3",
            align_items="center",
        ),
        blur_background(),
        id="navbar",
        height="80px",
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        align_items="center",
        spacing="6",
        padding="7px 20px 7px 20px;",  
    )
