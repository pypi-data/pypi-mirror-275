# Copyright (C) 2021-2023 Trevor Bayless <trevorbayless1@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from cli_chess.menus import MenuModel, MenuOption, MenuCategory
from enum import Enum


class OnlineGamesMenuOptions(Enum):
    CREATE_GAME = "Create a game"
    VS_COMPUTER_ONLINE = "Play vs Computer"
    WATCH_LICHESS_TV = "Watch Lichess TV"


class OnlineGamesMenuModel(MenuModel):
    def __init__(self):
        self.menu = self._create_menu()
        super().__init__(self.menu)

    @staticmethod
    def _create_menu() -> MenuCategory:
        """Create the menu options"""
        menu_options = [
            MenuOption(OnlineGamesMenuOptions.CREATE_GAME, "Create an online game against a random opponent"),
            MenuOption(OnlineGamesMenuOptions.VS_COMPUTER_ONLINE, "Play online against the computer"),
            MenuOption(OnlineGamesMenuOptions.WATCH_LICHESS_TV, "Watch top rated Lichess players compete live"),
        ]

        return MenuCategory("Online Games", menu_options)
