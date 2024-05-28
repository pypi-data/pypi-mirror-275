# Copyright (C) 2021-2024 Trevor Bayless <trevorbayless1@gmail.com>
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

from cli_chess.core.game import PlayableGameModelBase
from cli_chess.modules.engine import EngineModel
from cli_chess.core.game.game_options import GameOption
from cli_chess.utils.logging import log
from cli_chess.utils.config import player_info_config
from chess import COLOR_NAMES


class OfflineGameModel(PlayableGameModelBase):
    def __init__(self, game_parameters: dict):
        super().__init__(play_as_color=game_parameters[GameOption.COLOR],
                         variant=game_parameters[GameOption.VARIANT])

        self.engine_model = EngineModel(self.board_model, game_parameters)
        self.game_in_progress = True
        self._save_game_metadata(game_parameters=game_parameters)

    def update(self, **kwargs) -> None:
        """Called automatically as part of an event listener. This method
           listens to subscribed model update events and if deemed necessary
           triages and notifies listeners of the event.
        """
        super().update(**kwargs)
        if kwargs.get('isGameOver', False):
            self._report_game_over()

    def make_move(self, move: str):
        """Sends the move to the board model for it to be made"""
        if self.game_in_progress:
            try:
                if self.board_model.board.is_game_over():
                    self.game_in_progress = False
                    raise Warning("Game has already ended")

                if not self.is_my_turn():
                    raise Warning("Not your turn")

                self.board_model.make_move(move.strip())
                self.premove_model.clear_premove()

            except Exception:
                raise
        else:
            log.warning("Attempted to make a move in a game that's not in progress")
            raise Warning("Game has already ended")

    def set_premove(self, move: str) -> None:
        """Sets the premove"""
        self.premove_model.set_premove(move)

    def propose_takeback(self) -> None:
        """Take back the previous move"""
        try:
            if self.board_model.board.is_game_over():
                raise Warning("Game has already ended")

            self.premove_model.clear_premove()
            self.board_model.takeback(self.my_color)
        except Exception as e:
            log.error(f"Takeback failed - {e}")
            raise

    def offer_draw(self) -> None:
        raise Warning("Offline engine does not accept draw offers")

    def resign(self) -> None:
        """Handles resigning the game"""
        if self.game_in_progress:
            try:
                self.board_model.handle_resignation(self.my_color)
            except Exception:
                raise
        else:
            log.warning("Attempted to resign a game that's not in progress")
            raise Warning("Game has already ended")

    def _default_game_metadata(self) -> dict:
        """Returns the default structure for game metadata"""
        game_metadata = super()._default_game_metadata()
        game_metadata.update({
            'my_color_str': ""
        })
        return game_metadata

    def _save_game_metadata(self, **kwargs) -> None:
        """Parses and saves the data of the game being played"""
        try:
            if 'game_parameters' in kwargs:
                data = kwargs['game_parameters']
                self.game_metadata['my_color_str'] = COLOR_NAMES[self.my_color]
                self.game_metadata['variant'] = data[GameOption.VARIANT]

                # My player information
                my_name = player_info_config.get_value(player_info_config.Keys.OFFLINE_PLAYER_NAME)
                self.game_metadata['players'][COLOR_NAMES[self.my_color]]['title'] = ""
                self.game_metadata['players'][COLOR_NAMES[self.my_color]]['name'] = my_name
                self.game_metadata['players'][COLOR_NAMES[self.my_color]]['rating'] = ""

                # Engine information
                engine_name = "Fairy-Stockfish"  # TODO: Implement a better solution for when other engines are supported
                engine_name = engine_name + f" Lvl {data.get(GameOption.COMPUTER_SKILL_LEVEL)}" if not data.get(GameOption.SPECIFY_ELO) else engine_name  # noqa: E501
                self.game_metadata['players'][COLOR_NAMES[not self.my_color]]['title'] = ""
                self.game_metadata['players'][COLOR_NAMES[not self.my_color]]['name'] = engine_name
                self.game_metadata['players'][COLOR_NAMES[not self.my_color]]['rating'] = data.get(GameOption.COMPUTER_ELO, "")

            self._notify_game_model_updated()
        except KeyError as e:
            log.error(f"Error saving offline game metadata: {e}")

    def _report_game_over(self) -> None:
        """Saves game information and notifies listeners that the game has ended.
           This should only ever be called if the game is confirmed to be over
        """
        self.game_in_progress = False
        outcome = self.board_model.get_game_over_result()
        self.game_metadata['state']['status'] = outcome.termination
        self.game_metadata['state']['winner'] = COLOR_NAMES[outcome.winner]

        log.info(f"Game over (status={outcome.termination} winner={COLOR_NAMES[outcome.winner]})")
        self._notify_game_model_updated(offlineGameOver=True)
