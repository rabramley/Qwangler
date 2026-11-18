from pathlib import Path
from unittest.mock import MagicMock

import qwangler.cli as cli


def test_playback_uses_playsound_and_stops_previous_track(
    tmp_path: Path,
    monkeypatch,
) -> None:
    first_track = tmp_path / "first.mp3"
    first_track.touch()
    second_track = tmp_path / "second.mp3"
    second_track.touch()
    first_sound = MagicMock()
    second_sound = MagicMock()
    first_sound.is_alive.return_value = True
    second_sound.is_alive.return_value = True
    play = MagicMock(side_effect=[first_sound, second_sound])
    monkeypatch.setattr(cli, "playsound", play)
    app = cli.PlaylistApp()

    app.start_playing(first_track)
    app.start_playing(first_track)
    app.start_playing(second_track)

    assert play.call_count == 2
    play.assert_any_call(str(first_track.resolve()), block=False)
    play.assert_any_call(str(second_track.resolve()), block=False)
    first_sound.stop.assert_called_once()
    assert app._current_track == second_track.resolve()
    assert app._current_sound is second_sound
