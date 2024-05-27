from __future__ import annotations
import rio
from dataclasses import dataclass


from dataclasses import KW_ONLY, field, dataclass
from typing import *  # type: ignore
import rio


@dataclass
class NavigationLink:
    text: str
    icon: str
    target: str


NAVIGATION_LINKS = [
    NavigationLink("Home", "material/house", "/"),
    NavigationLink("My Agent", "material/person", "/agent"),
    NavigationLink("Fleet", "material/rocket", "/fleet"),
    NavigationLink("Systems", "material/wb-sunny", "/systems"),
    NavigationLink("Waypoints", "material/point-scan", "/waypoints"),
    NavigationLink("Factions", "material/groups", "/factions"),
    NavigationLink("Agent Roster", "material/emoji-people", "/roster"),
    NavigationLink("Stats", "material/query-stats", "/stats"),
]


class Navbar(rio.Component):
    is_open: bool = False

    def on_press_button(self) -> None:
        self.is_open = True if self.is_open is False else False

    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        self.on_press_button()

    def build(self) -> rio.Component:
        return rio.Popup(
            anchor=rio.Button("Data Sources", on_press=self.on_press_button),
            content=rio.Column(
                rio.Grid(
                    [rio.Text("Data Source 1"), rio.Switch()],
                    [rio.Text("Data Source 2"), rio.Switch()],
                    [rio.Text("Data Source 3"), rio.Switch()],
                    column_spacing=0.8,
                    row_spacing=0.8,
                ),
                margin=0.8,
            ),
            color="hud",
            position="bottom",
            is_open=self.is_open,
            align_x=0.5,
            align_y=0.5,
        )

        return rio.Card(
            rio.Markdown(
                """
Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

![Hägar](https://www.cameraegg.org/wp-content/uploads/2016/01/Nikon-D500-Sample-Images-2.jpg)

Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
"""
            ),
            color="hud",
            align_x=0.5,
            align_y=0.5,
        )


app = rio.App(
    build=lambda: Navbar(),
)
