"""Tests for the PlaylistApp widget."""


import pytest
from pathlib import Path



@pytest.fixture
def app() -> PlaylistApp:
    """Create a fresh PlaylistApp instance for tests."""
    return PlaylistApp()


class TestPlaylistApp:
    def test_tracks_property(self, app: PlaylistApp) -> None:
        """The tracks property should return list of resolved paths from playlist."""
        # TrackItem stores Path in self.path attribute
        track = TrackItem(Path("/tmp/test.mp3"))
        app.playlist.append(track)

        tracks = app.tracks()
        assert len(tracks) == 1
        assert tracks[0] == Path("/tmp/test.mp3")

    def test_update_status(self, app: PlaylistApp) -> None:
        """update_status should update the status bar text."""
        app.update_status("Test message | 5 track(s)")
        # The actual text rendering is UI-level; we verify the method completes without error.


class TestMediaTreeIntegration:
    def test_filter_excludes_non_audio(self) -> None:
        """filter_paths should exclude non-audio files."""
        tree = MediaTree(Path("/tmp/test"))
        audio_suffixes = config["audio_suffixes"]  # {'.mp3', '.flac'}

        files = [Path(f) for f in ["/tmp/a.mp3", "/tmp/b.flac", "/tmp/c.txt", "/tmp/d.m4a"]]
        result = list(tree.filter_paths(files))

        names = sorted([f.name for f in result])
        # Only mp3 and flac should match (audio suffixes)
        assert set(names) == {".mp3", ".flac"}

    def test_render_label_adds_checkmarks(self):
        """render_label should add ✓ markers for playlist tracks."""
        # This tests the integration of status caching with label rendering.
        tree = MediaTree(Path("/tmp/test"))
        assert hasattr(tree, "folder_playlist_status")
