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

from __future__ import annotations
from cli_chess.menus import MenuPresenter
from cli_chess.menus.settings_menu import SettingsMenuView
from cli_chess.menus.program_settings_menu import ProgramSettingsMenuModel, ProgramSettingsMenuPresenter
from cli_chess.modules.token_manager import TokenManagerPresenter
from cli_chess.modules.token_manager.token_manager_model import g_token_manager_model
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cli_chess.menus.settings_menu import SettingsMenuModel


class SettingsMenuPresenter(MenuPresenter):
    """Defines the settings menu"""
    def __init__(self, model: SettingsMenuModel):
        self.model = model
        self.token_manger_presenter = TokenManagerPresenter(g_token_manager_model)
        self.program_settings_menu_presenter = ProgramSettingsMenuPresenter(ProgramSettingsMenuModel())
        self.view = SettingsMenuView(self)
        super().__init__(self.model, self.view)
