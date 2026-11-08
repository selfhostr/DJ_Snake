"""Keyboard shortcuts of the clip page.

String-level checks on the clip page (web/index.html).
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "web" / "index.html").read_text(encoding="utf-8")


def test_page_has_help_dialog_and_button():
    assert '<dialog id="kbdlg"' in PAGE
    assert 'id="kbbtn"' in PAGE
    assert 'aria-haspopup="dialog"' in PAGE.split('id="kbbtn"')[1][:200]


def test_shortcut_map_documents_every_binding():
    block = PAGE.split("const SHORTCUTS = [", 1)[1].split("];", 1)[0]
    for label in (
        "kb_playpause kb_seekb kb_seekf kb_next kb_prev kb_shuffle kb_loop "
        "kb_mute kb_volup kb_voldn kb_fs kb_lyr kb_theme kb_help kb_esc"
    ).split():
        assert label in block


def test_help_strings_in_both_languages():
    en, fr = PAGE.split("    fr: {", 1)
    keys = {
        k
        for k in set(__import__("re").findall(r'"(kb_[a-z_]+)"', PAGE))
        if not k.endswith("_")
    }
    assert keys
    for key in keys:
        assert f"      {key}:" in en, key
        assert f"      {key}:" in fr, key


def test_listener_ignores_fields_and_modifiers():
    code = PAGE.split(
        'document.addEventListener("keydown", (e) => {\n    if (e.defaultPrevented || e.isComposing',
        1,
    )[1]
    head = code[:700]
    assert "e.ctrlKey || e.metaKey || e.altKey" in head
    assert "input, textarea, select" in head
    assert "contenteditable" in head
    assert "active()" in code  # control keys need a control link in voice


def test_layout_independent_matching():
    assert "function kbLetter" in PAGE
    assert 'e.key === "?"' in PAGE


def test_docs_list_shortcuts():
    for doc in (ROOT / "docs" / "source" / "clip-page.md",):
        text = doc.read_text(encoding="utf-8")
        assert "Keyboard shortcuts" in text, doc
