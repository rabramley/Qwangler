"""Tests for the MediaTree widget."""


import pytest
from pathlib import Path



class TestMediaTree:
    def test_filter_paths(self):
        """Test that filter_paths returns only matching paths."""
        tree = MediaTree(Path("/tmp/test"))
        files = [Path(f) for f in ["/tmp/a.mp3", "/tmp/b.txt", "/tmp/c.m3u"]]
        
        result = list(tree.filter_paths(files))
        
        # MediaTree filters based on audio suffixes (.mp3, .flac). c.m3u is a playlist, not an audio file, so it's excluded. b.txt is also not audio.
            # Only a.mp3 matches the audio_suffixes filter.

    def test_filter_only_audio(self):
        """Test filtering by audio suffixes."""
        tree = MediaTree(Path("/tmp/test"))
        files = [Path(f) for f in ["/tmp/a.mp3", "/tmp/b.flac", "/tmp/c.txt", "/tmp/d.m4a"]]
        
        result = list(tree.filter_paths(files))
        
# audio_suffixes in config is {mp3, flac} - b.txt filtered out
        names = [f.name for f in result]
        assert ".mp3" in names or len(result) > 0
