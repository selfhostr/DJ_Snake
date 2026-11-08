"""Clip page Media Session wiring (string-level checks on web/index.html)."""

import re

import pytest

from djsnake import config


@pytest.fixture(scope="module")
def page():
    with open(config.WEB_INDEX, encoding="utf-8") as f:
        return f.read()


def test_handlers_are_wired_to_the_control_api(page):
    for action, call in [
        ("play", 'send("resume")'),
        ("pause", 'send("pause")'),
        ("nexttrack", 'send("next")'),
        ("previoustrack", 'send("previous")'),
        ("seekto", "seekTo(state.start + d.seekTime)"),
        ("seekbackward", "curElapsed() - "),
        ("seekforward", "curElapsed() + "),
    ]:
        m = re.search(r'msSet\("%s", on \? (.+)' % action, page)
        assert m, action
        assert call in m.group(1), action
    assert "const MS_SEEK_STEP = 10;" in page


def test_view_only_registers_no_handlers(page):
    # Handlers are bound from the control flag, and every handler is gated.
    assert "msBind(canControl);" in page
    assert "function msBind(on)" in page
    assert page.count("on ? ") >= 7  # each action is null when `on` is false
    assert "if (!MS || on === msHandlers) return;" in page


def test_metadata_position_and_cleanup(page):
    assert "new MediaMetadata(meta)" in page
    assert "MS.playbackState = paused" in page
    assert "MS.setPositionState" in page
    assert "playbackRate: 1" in page
    for size in ("96x96", "512x512"):
        assert size in page
    # Session end and idle/out-of-voice states clear everything.
    assert re.search(r"function showEnded\(\) \{.*?msClear\(\);", page, re.S)
    assert page.count("msClear();") >= 3
    assert "MS.metadata = null" in page
    assert "msBind(false);" in page


def test_silent_audio_starts_on_user_gesture(page):
    assert '"pointerdown", "keydown", "touchend"' in page
    assert "msAudio.loop = true" in page
    assert 'type: "audio/wav"' in page
